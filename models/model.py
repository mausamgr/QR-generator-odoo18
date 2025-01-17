import base64
import uuid
from io import BytesIO

import qrcode

from odoo import fields, models


class AccountMoveInherit(models.Model):
    _inherit = 'account.move'

    qr_code = fields.Binary("QR Code", compute='generate_qr_code')


    def generate_qr_code(self):
        for rec in self:
            if rec.partner_id:
                if qrcode and base64:

                    base_url = f"{rec.env['ir.config_parameter'].sudo().get_param('web.base.url')}/my/invoices/{rec.id}"
                    
                    if not rec.access_token:
                        rec.access_token = str(uuid.uuid4())


                    # access_token = str(uuid.uuid4())


                    dynamic_url = f"{base_url}?access_token={rec.access_token}&payment=True#portal_pay"

                    qr = qrcode.QRCode(
                        version=1,
                        error_correction=qrcode.constants.ERROR_CORRECT_L,
                        box_size=3,
                        border=4,
                    )
                    qr.add_data(dynamic_url) 
                    qr.make(fit=True)
                    img = qr.make_image(fill='black', back_color='white')
                    

                    temp = BytesIO()
                    img.save(temp, format="PNG")
                    qr_image = base64.b64encode(temp.getvalue())

                    rec.qr_code = qr_image
