from . import base_types
from ._ISO2ALanguageCode import ISO2ALanguageCode
from ._Max256Text import Max256Text
from ._PhoneNumber import PhoneNumber

class ContactPersonal2(base_types._BaseFieldType):

	__slots__ = ["_BizEmail", "_BizFax", "_BizPhne", "_HomeFax", "_HomePhne", "_Lang", "_MobPhne", "_OthrEmail", "_OthrPhne", "_PrsnlEmail", "_URL"]
	@property
	def BizEmail(self):
		return self._BizEmail

	@BizEmail.setter
	def BizEmail(self, value):
		self._BizEmail = value if type(value) != base_types.auto else self.make_default("BizEmail")

	@BizEmail.deleter
	def BizEmail(self):
		del self._BizEmail
		self._BizEmail = None

	@property
	def BizFax(self):
		return self._BizFax

	@BizFax.setter
	def BizFax(self, value):
		self._BizFax = value if type(value) != base_types.auto else self.make_default("BizFax")

	@BizFax.deleter
	def BizFax(self):
		del self._BizFax
		self._BizFax = None

	@property
	def BizPhne(self):
		return self._BizPhne

	@BizPhne.setter
	def BizPhne(self, value):
		self._BizPhne = value if type(value) != base_types.auto else self.make_default("BizPhne")

	@BizPhne.deleter
	def BizPhne(self):
		del self._BizPhne
		self._BizPhne = None

	@property
	def HomeFax(self):
		return self._HomeFax

	@HomeFax.setter
	def HomeFax(self, value):
		self._HomeFax = value if type(value) != base_types.auto else self.make_default("HomeFax")

	@HomeFax.deleter
	def HomeFax(self):
		del self._HomeFax
		self._HomeFax = None

	@property
	def HomePhne(self):
		return self._HomePhne

	@HomePhne.setter
	def HomePhne(self, value):
		self._HomePhne = value if type(value) != base_types.auto else self.make_default("HomePhne")

	@HomePhne.deleter
	def HomePhne(self):
		del self._HomePhne
		self._HomePhne = None

	@property
	def Lang(self):
		return self._Lang

	@Lang.setter
	def Lang(self, value):
		self._Lang = value if type(value) != base_types.auto else self.make_default("Lang")

	@Lang.deleter
	def Lang(self):
		del self._Lang
		self._Lang = None

	@property
	def MobPhne(self):
		return self._MobPhne

	@MobPhne.setter
	def MobPhne(self, value):
		self._MobPhne = value if type(value) != base_types.auto else self.make_default("MobPhne")

	@MobPhne.deleter
	def MobPhne(self):
		del self._MobPhne
		self._MobPhne = None

	@property
	def OthrEmail(self):
		return self._OthrEmail

	@OthrEmail.setter
	def OthrEmail(self, value):
		self._OthrEmail = value if type(value) != base_types.auto else self.make_default("OthrEmail")

	@OthrEmail.deleter
	def OthrEmail(self):
		del self._OthrEmail
		self._OthrEmail = None

	@property
	def OthrPhne(self):
		return self._OthrPhne

	@OthrPhne.setter
	def OthrPhne(self, value):
		self._OthrPhne = value if type(value) != base_types.auto else self.make_default("OthrPhne")

	@OthrPhne.deleter
	def OthrPhne(self):
		del self._OthrPhne
		self._OthrPhne = None

	@property
	def PrsnlEmail(self):
		return self._PrsnlEmail

	@PrsnlEmail.setter
	def PrsnlEmail(self, value):
		self._PrsnlEmail = value if type(value) != base_types.auto else self.make_default("PrsnlEmail")

	@PrsnlEmail.deleter
	def PrsnlEmail(self):
		del self._PrsnlEmail
		self._PrsnlEmail = None

	@property
	def URL(self):
		return self._URL

	@URL.setter
	def URL(self, value):
		self._URL = value if type(value) != base_types.auto else self.make_default("URL")

	@URL.deleter
	def URL(self):
		del self._URL
		self._URL = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='BizEmail', type=Max256Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='BizFax', type=PhoneNumber, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='BizPhne', type=PhoneNumber, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='HomeFax', type=PhoneNumber, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='HomePhne', type=PhoneNumber, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Lang', type=ISO2ALanguageCode, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MobPhne', type=PhoneNumber, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OthrEmail', type=Max256Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OthrPhne', type=PhoneNumber, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrsnlEmail', type=Max256Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='URL', type=Max256Text, min=0, max=1, mutex_group=None, array=False),
	))

