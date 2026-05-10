import base_types
import PhoneNumber
import Max35Text
import Max70Text
import ISO2ALanguageCode
import Max256Text

class ContactBusiness1(base_types._BaseFieldType):

	__slots__ = ["_MddlNm", "_LastNm", "_Email", "_GvnNm", "_Phne", "_TollFreePhne", "_Lang", "_Nm", "_PrprtyPhne", "_URL", "_Fax"]
	@property
	def MddlNm(self):
		return self._MddlNm

	@MddlNm.setter
	def MddlNm(self, value):
		self._MddlNm = value if type(value) != auto else self.make_default("MddlNm")

	@MddlNm.deleter
	def MddlNm(self):
		del self._MddlNm
		self._MddlNm = None

	@property
	def LastNm(self):
		return self._LastNm

	@LastNm.setter
	def LastNm(self, value):
		self._LastNm = value if type(value) != auto else self.make_default("LastNm")

	@LastNm.deleter
	def LastNm(self):
		del self._LastNm
		self._LastNm = None

	@property
	def Email(self):
		return self._Email

	@Email.setter
	def Email(self, value):
		self._Email = value if type(value) != auto else self.make_default("Email")

	@Email.deleter
	def Email(self):
		del self._Email
		self._Email = None

	@property
	def GvnNm(self):
		return self._GvnNm

	@GvnNm.setter
	def GvnNm(self, value):
		self._GvnNm = value if type(value) != auto else self.make_default("GvnNm")

	@GvnNm.deleter
	def GvnNm(self):
		del self._GvnNm
		self._GvnNm = None

	@property
	def Phne(self):
		return self._Phne

	@Phne.setter
	def Phne(self, value):
		self._Phne = value if type(value) != auto else self.make_default("Phne")

	@Phne.deleter
	def Phne(self):
		del self._Phne
		self._Phne = None

	@property
	def TollFreePhne(self):
		return self._TollFreePhne

	@TollFreePhne.setter
	def TollFreePhne(self, value):
		self._TollFreePhne = value if type(value) != auto else self.make_default("TollFreePhne")

	@TollFreePhne.deleter
	def TollFreePhne(self):
		del self._TollFreePhne
		self._TollFreePhne = None

	@property
	def Lang(self):
		return self._Lang

	@Lang.setter
	def Lang(self, value):
		self._Lang = value if type(value) != auto else self.make_default("Lang")

	@Lang.deleter
	def Lang(self):
		del self._Lang
		self._Lang = None

	@property
	def Nm(self):
		return self._Nm

	@Nm.setter
	def Nm(self, value):
		self._Nm = value if type(value) != auto else self.make_default("Nm")

	@Nm.deleter
	def Nm(self):
		del self._Nm
		self._Nm = None

	@property
	def PrprtyPhne(self):
		return self._PrprtyPhne

	@PrprtyPhne.setter
	def PrprtyPhne(self, value):
		self._PrprtyPhne = value if type(value) != auto else self.make_default("PrprtyPhne")

	@PrprtyPhne.deleter
	def PrprtyPhne(self):
		del self._PrprtyPhne
		self._PrprtyPhne = None

	@property
	def URL(self):
		return self._URL

	@URL.setter
	def URL(self, value):
		self._URL = value if type(value) != auto else self.make_default("URL")

	@URL.deleter
	def URL(self):
		del self._URL
		self._URL = None

	@property
	def Fax(self):
		return self._Fax

	@Fax.setter
	def Fax(self, value):
		self._Fax = value if type(value) != auto else self.make_default("Fax")

	@Fax.deleter
	def Fax(self):
		del self._Fax
		self._Fax = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='MddlNm', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='LastNm', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Email', type=Max256Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='GvnNm', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Phne', type=PhoneNumber, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TollFreePhne', type=PhoneNumber, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Lang', type=ISO2ALanguageCode, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Nm', type=Max70Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrprtyPhne', type=PhoneNumber, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='URL', type=Max256Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Fax', type=PhoneNumber, min=0, max=1, mutex_group=None, array=False),
	))

