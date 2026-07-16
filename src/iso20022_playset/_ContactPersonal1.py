# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ISO2ALanguageCode
from . import Max256Text
from . import Max35Text
from . import Max70Text
from . import PhoneNumber

class ContactPersonal1(base_types._BaseFieldType):

	__slots__ = ["_BizEmail", "_BizFax", "_BizPhne", "_GvnNm", "_HomeFax", "_HomePhne", "_Lang", "_LastNm", "_MddlNm", "_MobPhne", "_Nm", "_OthrEmail", "_OthrPhne", "_PrsnlEmail", "_URL"]
	@property
	def BizEmail(self):
		return self._BizEmail

	@BizEmail.setter
	def BizEmail(self, value):
		self._BizEmail = value if value is not None else base_types.UninitialisedField(self, 'BizEmail', Max256Text, False)

	@BizEmail.deleter
	def BizEmail(self):
		del self._BizEmail
		self._BizEmail = base_types.UninitialisedField(self, 'BizEmail', Max256Text, False)

	@property
	def BizFax(self):
		return self._BizFax

	@BizFax.setter
	def BizFax(self, value):
		self._BizFax = value if value is not None else base_types.UninitialisedField(self, 'BizFax', PhoneNumber, False)

	@BizFax.deleter
	def BizFax(self):
		del self._BizFax
		self._BizFax = base_types.UninitialisedField(self, 'BizFax', PhoneNumber, False)

	@property
	def BizPhne(self):
		return self._BizPhne

	@BizPhne.setter
	def BizPhne(self, value):
		self._BizPhne = value if value is not None else base_types.UninitialisedField(self, 'BizPhne', PhoneNumber, False)

	@BizPhne.deleter
	def BizPhne(self):
		del self._BizPhne
		self._BizPhne = base_types.UninitialisedField(self, 'BizPhne', PhoneNumber, False)

	@property
	def GvnNm(self):
		return self._GvnNm

	@GvnNm.setter
	def GvnNm(self, value):
		self._GvnNm = value if value is not None else base_types.UninitialisedField(self, 'GvnNm', Max35Text, False)

	@GvnNm.deleter
	def GvnNm(self):
		del self._GvnNm
		self._GvnNm = base_types.UninitialisedField(self, 'GvnNm', Max35Text, False)

	@property
	def HomeFax(self):
		return self._HomeFax

	@HomeFax.setter
	def HomeFax(self, value):
		self._HomeFax = value if value is not None else base_types.UninitialisedField(self, 'HomeFax', PhoneNumber, False)

	@HomeFax.deleter
	def HomeFax(self):
		del self._HomeFax
		self._HomeFax = base_types.UninitialisedField(self, 'HomeFax', PhoneNumber, False)

	@property
	def HomePhne(self):
		return self._HomePhne

	@HomePhne.setter
	def HomePhne(self, value):
		self._HomePhne = value if value is not None else base_types.UninitialisedField(self, 'HomePhne', PhoneNumber, False)

	@HomePhne.deleter
	def HomePhne(self):
		del self._HomePhne
		self._HomePhne = base_types.UninitialisedField(self, 'HomePhne', PhoneNumber, False)

	@property
	def Lang(self):
		return self._Lang

	@Lang.setter
	def Lang(self, value):
		self._Lang = value if value is not None else base_types.UninitialisedField(self, 'Lang', ISO2ALanguageCode, False)

	@Lang.deleter
	def Lang(self):
		del self._Lang
		self._Lang = base_types.UninitialisedField(self, 'Lang', ISO2ALanguageCode, False)

	@property
	def LastNm(self):
		return self._LastNm

	@LastNm.setter
	def LastNm(self, value):
		self._LastNm = value if value is not None else base_types.UninitialisedField(self, 'LastNm', Max35Text, False)

	@LastNm.deleter
	def LastNm(self):
		del self._LastNm
		self._LastNm = base_types.UninitialisedField(self, 'LastNm', Max35Text, False)

	@property
	def MddlNm(self):
		return self._MddlNm

	@MddlNm.setter
	def MddlNm(self, value):
		self._MddlNm = value if value is not None else base_types.UninitialisedField(self, 'MddlNm', Max35Text, False)

	@MddlNm.deleter
	def MddlNm(self):
		del self._MddlNm
		self._MddlNm = base_types.UninitialisedField(self, 'MddlNm', Max35Text, False)

	@property
	def MobPhne(self):
		return self._MobPhne

	@MobPhne.setter
	def MobPhne(self, value):
		self._MobPhne = value if value is not None else base_types.UninitialisedField(self, 'MobPhne', PhoneNumber, False)

	@MobPhne.deleter
	def MobPhne(self):
		del self._MobPhne
		self._MobPhne = base_types.UninitialisedField(self, 'MobPhne', PhoneNumber, False)

	@property
	def Nm(self):
		return self._Nm

	@Nm.setter
	def Nm(self, value):
		self._Nm = value if value is not None else base_types.UninitialisedField(self, 'Nm', Max70Text, False)

	@Nm.deleter
	def Nm(self):
		del self._Nm
		self._Nm = base_types.UninitialisedField(self, 'Nm', Max70Text, False)

	@property
	def OthrEmail(self):
		return self._OthrEmail

	@OthrEmail.setter
	def OthrEmail(self, value):
		self._OthrEmail = value if value is not None else base_types.UninitialisedField(self, 'OthrEmail', Max256Text, False)

	@OthrEmail.deleter
	def OthrEmail(self):
		del self._OthrEmail
		self._OthrEmail = base_types.UninitialisedField(self, 'OthrEmail', Max256Text, False)

	@property
	def OthrPhne(self):
		return self._OthrPhne

	@OthrPhne.setter
	def OthrPhne(self, value):
		self._OthrPhne = value if value is not None else base_types.UninitialisedField(self, 'OthrPhne', PhoneNumber, False)

	@OthrPhne.deleter
	def OthrPhne(self):
		del self._OthrPhne
		self._OthrPhne = base_types.UninitialisedField(self, 'OthrPhne', PhoneNumber, False)

	@property
	def PrsnlEmail(self):
		return self._PrsnlEmail

	@PrsnlEmail.setter
	def PrsnlEmail(self, value):
		self._PrsnlEmail = value if value is not None else base_types.UninitialisedField(self, 'PrsnlEmail', Max256Text, False)

	@PrsnlEmail.deleter
	def PrsnlEmail(self):
		del self._PrsnlEmail
		self._PrsnlEmail = base_types.UninitialisedField(self, 'PrsnlEmail', Max256Text, False)

	@property
	def URL(self):
		return self._URL

	@URL.setter
	def URL(self, value):
		self._URL = value if value is not None else base_types.UninitialisedField(self, 'URL', Max256Text, False)

	@URL.deleter
	def URL(self):
		del self._URL
		self._URL = base_types.UninitialisedField(self, 'URL', Max256Text, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='BizEmail', type=Max256Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='BizFax', type=PhoneNumber, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='BizPhne', type=PhoneNumber, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='GvnNm', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='HomeFax', type=PhoneNumber, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='HomePhne', type=PhoneNumber, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Lang', type=ISO2ALanguageCode, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='LastNm', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MddlNm', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MobPhne', type=PhoneNumber, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Nm', type=Max70Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OthrEmail', type=Max256Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OthrPhne', type=PhoneNumber, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrsnlEmail', type=Max256Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='URL', type=Max256Text, min=0, max=1, mutex_group=None, array=False),
	))