# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ISO2ALanguageCode
from . import Max256Text
from . import Max35Text
from . import Max70Text
from . import PhoneNumber

class ContactBusiness1(base_types._BaseFieldType):

	__slots__ = ["_Email", "_Fax", "_GvnNm", "_Lang", "_LastNm", "_MddlNm", "_Nm", "_Phne", "_PrprtyPhne", "_TollFreePhne", "_URL"]
	@property
	def Email(self):
		return self._Email

	@Email.setter
	def Email(self, value):
		self._Email = value if value is not None else base_types.UninitialisedField(self, 'Email', Max256Text, False)

	@Email.deleter
	def Email(self):
		del self._Email
		self._Email = base_types.UninitialisedField(self, 'Email', Max256Text, False)

	@property
	def Fax(self):
		return self._Fax

	@Fax.setter
	def Fax(self, value):
		self._Fax = value if value is not None else base_types.UninitialisedField(self, 'Fax', PhoneNumber, False)

	@Fax.deleter
	def Fax(self):
		del self._Fax
		self._Fax = base_types.UninitialisedField(self, 'Fax', PhoneNumber, False)

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
	def Phne(self):
		return self._Phne

	@Phne.setter
	def Phne(self, value):
		self._Phne = value if value is not None else base_types.UninitialisedField(self, 'Phne', PhoneNumber, False)

	@Phne.deleter
	def Phne(self):
		del self._Phne
		self._Phne = base_types.UninitialisedField(self, 'Phne', PhoneNumber, False)

	@property
	def PrprtyPhne(self):
		return self._PrprtyPhne

	@PrprtyPhne.setter
	def PrprtyPhne(self, value):
		self._PrprtyPhne = value if value is not None else base_types.UninitialisedField(self, 'PrprtyPhne', PhoneNumber, False)

	@PrprtyPhne.deleter
	def PrprtyPhne(self):
		del self._PrprtyPhne
		self._PrprtyPhne = base_types.UninitialisedField(self, 'PrprtyPhne', PhoneNumber, False)

	@property
	def TollFreePhne(self):
		return self._TollFreePhne

	@TollFreePhne.setter
	def TollFreePhne(self, value):
		self._TollFreePhne = value if value is not None else base_types.UninitialisedField(self, 'TollFreePhne', PhoneNumber, False)

	@TollFreePhne.deleter
	def TollFreePhne(self):
		del self._TollFreePhne
		self._TollFreePhne = base_types.UninitialisedField(self, 'TollFreePhne', PhoneNumber, False)

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
		base_types.FieldEntry(name='Email', type=Max256Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Fax', type=PhoneNumber, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='GvnNm', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Lang', type=ISO2ALanguageCode, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='LastNm', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MddlNm', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Nm', type=Max70Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Phne', type=PhoneNumber, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrprtyPhne', type=PhoneNumber, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TollFreePhne', type=PhoneNumber, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='URL', type=Max256Text, min=0, max=1, mutex_group=None, array=False),
	))