# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import Counterparty45
from . import Counterparty46
from . import OrganisationIdentification15Choice
from . import PartyIdentification248Choice
from . import TradeCounterpartyRelationshipRecord1

class TradeCounterpartyReport20(base_types._BaseFieldType):

	__slots__ = ["_Bnfcry", "_Brkr", "_ClrMmb", "_ExctnAgt", "_NttyRspnsblForRpt", "_OthrCtrPty", "_RltshRcrd", "_RptgCtrPty", "_SubmitgAgt"]
	@property
	def Bnfcry(self):
		return self._Bnfcry

	@Bnfcry.setter
	def Bnfcry(self, value):
		self._Bnfcry = value if value is not None else base_types.UninitialisedField(self, 'Bnfcry', PartyIdentification248Choice, True)

	@Bnfcry.deleter
	def Bnfcry(self):
		del self._Bnfcry
		self._Bnfcry = base_types.UninitialisedField(self, 'Bnfcry', PartyIdentification248Choice, True)

	@property
	def Brkr(self):
		return self._Brkr

	@Brkr.setter
	def Brkr(self, value):
		self._Brkr = value if value is not None else base_types.UninitialisedField(self, 'Brkr', OrganisationIdentification15Choice, False)

	@Brkr.deleter
	def Brkr(self):
		del self._Brkr
		self._Brkr = base_types.UninitialisedField(self, 'Brkr', OrganisationIdentification15Choice, False)

	@property
	def ClrMmb(self):
		return self._ClrMmb

	@ClrMmb.setter
	def ClrMmb(self, value):
		self._ClrMmb = value if value is not None else base_types.UninitialisedField(self, 'ClrMmb', PartyIdentification248Choice, False)

	@ClrMmb.deleter
	def ClrMmb(self):
		del self._ClrMmb
		self._ClrMmb = base_types.UninitialisedField(self, 'ClrMmb', PartyIdentification248Choice, False)

	@property
	def ExctnAgt(self):
		return self._ExctnAgt

	@ExctnAgt.setter
	def ExctnAgt(self, value):
		self._ExctnAgt = value if value is not None else base_types.UninitialisedField(self, 'ExctnAgt', OrganisationIdentification15Choice, True)

	@ExctnAgt.deleter
	def ExctnAgt(self):
		del self._ExctnAgt
		self._ExctnAgt = base_types.UninitialisedField(self, 'ExctnAgt', OrganisationIdentification15Choice, True)

	@property
	def NttyRspnsblForRpt(self):
		return self._NttyRspnsblForRpt

	@NttyRspnsblForRpt.setter
	def NttyRspnsblForRpt(self, value):
		self._NttyRspnsblForRpt = value if value is not None else base_types.UninitialisedField(self, 'NttyRspnsblForRpt', OrganisationIdentification15Choice, False)

	@NttyRspnsblForRpt.deleter
	def NttyRspnsblForRpt(self):
		del self._NttyRspnsblForRpt
		self._NttyRspnsblForRpt = base_types.UninitialisedField(self, 'NttyRspnsblForRpt', OrganisationIdentification15Choice, False)

	@property
	def OthrCtrPty(self):
		return self._OthrCtrPty

	@OthrCtrPty.setter
	def OthrCtrPty(self, value):
		self._OthrCtrPty = value if value is not None else base_types.UninitialisedField(self, 'OthrCtrPty', Counterparty46, False)

	@OthrCtrPty.deleter
	def OthrCtrPty(self):
		del self._OthrCtrPty
		self._OthrCtrPty = base_types.UninitialisedField(self, 'OthrCtrPty', Counterparty46, False)

	@property
	def RltshRcrd(self):
		return self._RltshRcrd

	@RltshRcrd.setter
	def RltshRcrd(self, value):
		self._RltshRcrd = value if value is not None else base_types.UninitialisedField(self, 'RltshRcrd', TradeCounterpartyRelationshipRecord1, True)

	@RltshRcrd.deleter
	def RltshRcrd(self):
		del self._RltshRcrd
		self._RltshRcrd = base_types.UninitialisedField(self, 'RltshRcrd', TradeCounterpartyRelationshipRecord1, True)

	@property
	def RptgCtrPty(self):
		return self._RptgCtrPty

	@RptgCtrPty.setter
	def RptgCtrPty(self, value):
		self._RptgCtrPty = value if value is not None else base_types.UninitialisedField(self, 'RptgCtrPty', Counterparty45, False)

	@RptgCtrPty.deleter
	def RptgCtrPty(self):
		del self._RptgCtrPty
		self._RptgCtrPty = base_types.UninitialisedField(self, 'RptgCtrPty', Counterparty45, False)

	@property
	def SubmitgAgt(self):
		return self._SubmitgAgt

	@SubmitgAgt.setter
	def SubmitgAgt(self, value):
		self._SubmitgAgt = value if value is not None else base_types.UninitialisedField(self, 'SubmitgAgt', OrganisationIdentification15Choice, False)

	@SubmitgAgt.deleter
	def SubmitgAgt(self):
		del self._SubmitgAgt
		self._SubmitgAgt = base_types.UninitialisedField(self, 'SubmitgAgt', OrganisationIdentification15Choice, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Bnfcry', type=PartyIdentification248Choice, min=0, max=2, mutex_group=None, array=True),
		base_types.FieldEntry(name='Brkr', type=OrganisationIdentification15Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ClrMmb', type=PartyIdentification248Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ExctnAgt', type=OrganisationIdentification15Choice, min=0, max=2, mutex_group=None, array=True),
		base_types.FieldEntry(name='NttyRspnsblForRpt', type=OrganisationIdentification15Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OthrCtrPty', type=Counterparty46, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RltshRcrd', type=TradeCounterpartyRelationshipRecord1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='RptgCtrPty', type=Counterparty45, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SubmitgAgt', type=OrganisationIdentification15Choice, min=0, max=1, mutex_group=None, array=False),
	))