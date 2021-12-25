import platform
import requests
imoort sys
z = platform.release().replace('.', '').replace(' ', '').replace('-', '').replace(':', '').replace('#', '')[::-1].upper()+platform.version().replace('.', '').replace(' ', '').replace('-', '').replace(':', '').replace('#', '')[::-1].upper()+platform.platform().replace('.', '').replace(' ', '').replace('-', '').replace(':', '').replace('#', '')[::-1].upper()+platform.system().replace('.', '').replace(' ', '').replace('-', '').replace(':', '').replace('#', '')[::-1].upper()

print z
print z
