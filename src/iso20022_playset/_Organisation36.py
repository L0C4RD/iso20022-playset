# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import CountryCode
from . import ISODate
from . import Max140Text
from . import Max35Text
from . import PartyIdentification140
from . import PostalAddress1

class Organisation36(base_types._BaseFieldType):

	__slots__ = ["_CorpInvstrAdr", "_Id", "_Nm", "_NtlRegnNb", "_Purp", "_RegnCtry", "_RegnDt", "_TaxIdNb", "_TaxtnCtry"]
	@property
	def CorpInvstrAdr(self):
		return self._CorpInvstrAdr

	@CorpInvstrAdr.setter
	def CorpInvstrAdr(self, value):
		self._CorpInvstrAdr = value if value is not None else base_types.UninitialisedField(self, 'CorpInvstrAdr', PostalAddress1, False)

	@CorpInvstrAdr.deleter
	def CorpInvstrAdr(self):
		del self._CorpInvstrAdr
		self._CorpInvstrAdr = base_types.UninitialisedField(self, 'CorpInvstrAdr', PostalAddress1, False)

	@property
	def Id(self):
		return self._Id

	@Id.setter
	def Id(self, value):
		self._Id = value if value is not None else base_types.UninitialisedField(self, 'Id', PartyIdentification140, False)

	@Id.deleter
	def Id(self):
		del self._Id
		self._Id = base_types.UninitialisedField(self, 'Id', PartyIdentification140, False)

	@property
	def Nm(self):
		return self._Nm

	@Nm.setter
	def Nm(self, value):
		self._Nm = value if value is not None else base_types.UninitialisedField(self, 'Nm', Max140Text, False)

	@Nm.deleter
	def Nm(self):
		del self._Nm
		self._Nm = base_types.UninitialisedField(self, 'Nm', Max140Text, False)

	@property
	def NtlRegnNb(self):
		return self._NtlRegnNb

	@NtlRegnNb.setter
	def NtlRegnNb(self, value):
		self._NtlRegnNb = value if value is not None else base_types.UninitialisedField(self, 'NtlRegnNb', Max35Text, False)

	@NtlRegnNb.deleter
	def NtlRegnNb(self):
		del self._NtlRegnNb
		self._NtlRegnNb = base_types.UninitialisedField(self, 'NtlRegnNb', Max35Text, False)

	@property
	def Purp(self):
		return self._Purp

	@Purp.setter
	def Purp(self, value):
		self._Purp = value if value is not None else base_types.UninitialisedField(self, 'Purp', Max35Text, False)

	@Purp.deleter
	def Purp(self):
		del self._Purp
		self._Purp = base_types.UninitialisedField(self, 'Purp', Max35Text, False)

	@property
	def RegnCtry(self):
		return self._RegnCtry

	@RegnCtry.setter
	def RegnCtry(self, value):
		self._RegnCtry = value if value is not None else base_types.UninitialisedField(self, 'RegnCtry', CountryCode, False)

	@RegnCtry.deleter
	def RegnCtry(self):
		del self._RegnCtry
		self._RegnCtry = base_types.UninitialisedField(self, 'RegnCtry', CountryCode, False)

	@property
	def RegnDt(self):
		return self._RegnDt

	@RegnDt.setter
	def RegnDt(self, value):
		self._RegnDt = value if value is not None else base_types.UninitialisedField(self, 'RegnDt', ISODate, False)

	@RegnDt.deleter
	def RegnDt(self):
		del self._RegnDt
		self._RegnDt = base_types.UninitialisedField(self, 'RegnDt', ISODate, False)

	@property
	def TaxIdNb(self):
		return self._TaxIdNb

	@TaxIdNb.setter
	def TaxIdNb(self, value):
		self._TaxIdNb = value if value is not None else base_types.UninitialisedField(self, 'TaxIdNb', Max35Text, False)

	@TaxIdNb.deleter
	def TaxIdNb(self):
		del self._TaxIdNb
		self._TaxIdNb = base_types.UninitialisedField(self, 'TaxIdNb', Max35Text, False)

	@property
	def TaxtnCtry(self):
		return self._TaxtnCtry

	@TaxtnCtry.setter
	def TaxtnCtry(self, value):
		self._TaxtnCtry = value if value is not None else base_types.UninitialisedField(self, 'TaxtnCtry', CountryCode, False)

	@TaxtnCtry.deleter
	def TaxtnCtry(self):
		del self._TaxtnCtry
		self._TaxtnCtry = base_types.UninitialisedField(self, 'TaxtnCtry', CountryCode, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='CorpInvstrAdr', type=PostalAddress1, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Id', type=PartyIdentification140, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Nm', type=Max140Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NtlRegnNb', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Purp', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RegnCtry', type=CountryCode, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RegnDt', type=ISODate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TaxIdNb', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TaxtnCtry', type=CountryCode, min=0, max=1, mutex_group=None, array=False),
	))