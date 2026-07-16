# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import PartyIdentification242Choice

class SettlementParties120(base_types._BaseFieldType):

	__slots__ = ["_BnfcryInstn", "_DlvryAgt", "_Intrmy", "_RcvgAgt"]
	@property
	def BnfcryInstn(self):
		return self._BnfcryInstn

	@BnfcryInstn.setter
	def BnfcryInstn(self, value):
		self._BnfcryInstn = value if value is not None else base_types.UninitialisedField(self, 'BnfcryInstn', PartyIdentification242Choice, False)

	@BnfcryInstn.deleter
	def BnfcryInstn(self):
		del self._BnfcryInstn
		self._BnfcryInstn = base_types.UninitialisedField(self, 'BnfcryInstn', PartyIdentification242Choice, False)

	@property
	def DlvryAgt(self):
		return self._DlvryAgt

	@DlvryAgt.setter
	def DlvryAgt(self, value):
		self._DlvryAgt = value if value is not None else base_types.UninitialisedField(self, 'DlvryAgt', PartyIdentification242Choice, False)

	@DlvryAgt.deleter
	def DlvryAgt(self):
		del self._DlvryAgt
		self._DlvryAgt = base_types.UninitialisedField(self, 'DlvryAgt', PartyIdentification242Choice, False)

	@property
	def Intrmy(self):
		return self._Intrmy

	@Intrmy.setter
	def Intrmy(self, value):
		self._Intrmy = value if value is not None else base_types.UninitialisedField(self, 'Intrmy', PartyIdentification242Choice, False)

	@Intrmy.deleter
	def Intrmy(self):
		del self._Intrmy
		self._Intrmy = base_types.UninitialisedField(self, 'Intrmy', PartyIdentification242Choice, False)

	@property
	def RcvgAgt(self):
		return self._RcvgAgt

	@RcvgAgt.setter
	def RcvgAgt(self, value):
		self._RcvgAgt = value if value is not None else base_types.UninitialisedField(self, 'RcvgAgt', PartyIdentification242Choice, False)

	@RcvgAgt.deleter
	def RcvgAgt(self):
		del self._RcvgAgt
		self._RcvgAgt = base_types.UninitialisedField(self, 'RcvgAgt', PartyIdentification242Choice, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='BnfcryInstn', type=PartyIdentification242Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DlvryAgt', type=PartyIdentification242Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Intrmy', type=PartyIdentification242Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RcvgAgt', type=PartyIdentification242Choice, min=1, max=1, mutex_group=None, array=False),
	))