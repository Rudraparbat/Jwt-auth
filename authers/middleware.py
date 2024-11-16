from django.utils.deprecation import MiddlewareMixin
# my customized middleware for getting ip address
class ipMidleware(MiddlewareMixin) :
    def process_request(self , request) :
        get_ip_address = request.META.get('HTTP_X_FORWARDED_FOR')
        if get_ip_address :
            ip = get_ip_address.split(',')[0]
        else :
            ip = request.META.get('REMOTE_ADDR')
        request.ip_address = ip


