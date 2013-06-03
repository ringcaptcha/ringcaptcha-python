from lib.Ringcaptcha import Ringcaptcha

lib = Ringcaptcha('XXXX','YYYY')
print lib.isValid('1234 ','efkwnof2345i43it43ot435')
print ', '.join("%s: %s" % item for item in vars(lib).items())