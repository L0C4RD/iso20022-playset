# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import CommunicationAddress3
from . import CountryCode
from . import ISODate
from . import Max140Text
from . import Max35Text
from . import PartyIdentification177Choice
from . import PostalAddress3

class Organisation38(base_types._BaseFieldType):

	__slots__ = ["_Id", "_Nm", "_NtlRegnNb", "_PmryComAdr", "_PstlAdr", "_Purp", "_RegnCtry", "_RegnDt", "_ScndryComAdr", "_TaxIdNb", "_TaxtnCtry"]
	@property
	def Id(self):
		return self._Id

	@Id.setter
	def Id(self, value):
		self._Id = value if value is not None else base_types.UninitialisedField(self, 'Id', PartyIdentification177Choice, False)

	@Id.deleter
	def Id(self):
		del self._Id
		self._Id = base_types.UninitialisedField(self, 'Id', PartyIdentification177Choice, False)

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
	def PmryComAdr(self):
		return self._PmryComAdr

	@PmryComAdr.setter
	def PmryComAdr(self, value):
		self._PmryComAdr = value if value is not None else base_types.UninitialisedField(self, 'PmryComAdr', CommunicationAddress3, False)

	@PmryComAdr.deleter
	def PmryComAdr(self):
		del self._PmryComAdr
		self._PmryComAdr = base_types.UninitialisedField(self, 'PmryComAdr', CommunicationAddress3, False)

	@property
	def PstlAdr(self):
		return self._PstlAdr

	@PstlAdr.setter
	def PstlAdr(self, value):
		self._PstlAdr = value if value is not None else base_types.UninitialisedField(self, 'PstlAdr', PostalAddress3, True)

	@PstlAdr.deleter
	def PstlAdr(self):
		del self._PstlAdr
		self._PstlAdr = base_types.UninitialisedField(self, 'PstlAdr', PostalAddress3, True)

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
	def ScndryComAdr(self):
		return self._ScndryComAdr

	@ScndryComAdr.setter
	def ScndryComAdr(self, value):
		self._ScndryComAdr = value if value is not None else base_types.UninitialisedField(self, 'ScndryComAdr', CommunicationAddress3, False)

	@ScndryComAdr.deleter
	def ScndryComAdr(self):
		del self._ScndryComAdr
		self._ScndryComAdr = base_types.UninitialisedField(self, 'ScndryComAdr', CommunicationAddress3, False)

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
		base_types.FieldEntry(name='Id', type=PartyIdentification177Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Nm', type=Max140Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NtlRegnNb', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PmryComAdr', type=CommunicationAddress3, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PstlAdr', type=PostalAddress3, min=1, max=5, mutex_group=None, array=True),
		base_types.FieldEntry(name='Purp', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RegnCtry', type=CountryCode, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RegnDt', type=ISODate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ScndryComAdr', type=CommunicationAddress3, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TaxIdNb', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TaxtnCtry', type=CountryCode, min=0, max=1, mutex_group=None, array=False),
	))