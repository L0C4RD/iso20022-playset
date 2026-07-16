# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ActiveCurrencyAndAmount
from . import FinancialInstitutionIdentification6
from . import ISODateTime
from . import Max105Text
from . import Max15NumericText
from . import Max35Text
from . import PartyIdentificationAndAccount6

class CancellationRequestInformation1(base_types._BaseFieldType):

	__slots__ = ["_CxlRsn", "_FincgRqstr", "_FrstAgt", "_IntrmyAgt", "_NbOfInvcReqs", "_OrgnlCreDtTm", "_OrgnlGrpId", "_TtlBlkInvcAmt"]
	@property
	def CxlRsn(self):
		return self._CxlRsn

	@CxlRsn.setter
	def CxlRsn(self, value):
		self._CxlRsn = value if value is not None else base_types.UninitialisedField(self, 'CxlRsn', Max105Text, False)

	@CxlRsn.deleter
	def CxlRsn(self):
		del self._CxlRsn
		self._CxlRsn = base_types.UninitialisedField(self, 'CxlRsn', Max105Text, False)

	@property
	def FincgRqstr(self):
		return self._FincgRqstr

	@FincgRqstr.setter
	def FincgRqstr(self, value):
		self._FincgRqstr = value if value is not None else base_types.UninitialisedField(self, 'FincgRqstr', PartyIdentificationAndAccount6, False)

	@FincgRqstr.deleter
	def FincgRqstr(self):
		del self._FincgRqstr
		self._FincgRqstr = base_types.UninitialisedField(self, 'FincgRqstr', PartyIdentificationAndAccount6, False)

	@property
	def FrstAgt(self):
		return self._FrstAgt

	@FrstAgt.setter
	def FrstAgt(self, value):
		self._FrstAgt = value if value is not None else base_types.UninitialisedField(self, 'FrstAgt', FinancialInstitutionIdentification6, False)

	@FrstAgt.deleter
	def FrstAgt(self):
		del self._FrstAgt
		self._FrstAgt = base_types.UninitialisedField(self, 'FrstAgt', FinancialInstitutionIdentification6, False)

	@property
	def IntrmyAgt(self):
		return self._IntrmyAgt

	@IntrmyAgt.setter
	def IntrmyAgt(self, value):
		self._IntrmyAgt = value if value is not None else base_types.UninitialisedField(self, 'IntrmyAgt', FinancialInstitutionIdentification6, False)

	@IntrmyAgt.deleter
	def IntrmyAgt(self):
		del self._IntrmyAgt
		self._IntrmyAgt = base_types.UninitialisedField(self, 'IntrmyAgt', FinancialInstitutionIdentification6, False)

	@property
	def NbOfInvcReqs(self):
		return self._NbOfInvcReqs

	@NbOfInvcReqs.setter
	def NbOfInvcReqs(self, value):
		self._NbOfInvcReqs = value if value is not None else base_types.UninitialisedField(self, 'NbOfInvcReqs', Max15NumericText, False)

	@NbOfInvcReqs.deleter
	def NbOfInvcReqs(self):
		del self._NbOfInvcReqs
		self._NbOfInvcReqs = base_types.UninitialisedField(self, 'NbOfInvcReqs', Max15NumericText, False)

	@property
	def OrgnlCreDtTm(self):
		return self._OrgnlCreDtTm

	@OrgnlCreDtTm.setter
	def OrgnlCreDtTm(self, value):
		self._OrgnlCreDtTm = value if value is not None else base_types.UninitialisedField(self, 'OrgnlCreDtTm', ISODateTime, False)

	@OrgnlCreDtTm.deleter
	def OrgnlCreDtTm(self):
		del self._OrgnlCreDtTm
		self._OrgnlCreDtTm = base_types.UninitialisedField(self, 'OrgnlCreDtTm', ISODateTime, False)

	@property
	def OrgnlGrpId(self):
		return self._OrgnlGrpId

	@OrgnlGrpId.setter
	def OrgnlGrpId(self, value):
		self._OrgnlGrpId = value if value is not None else base_types.UninitialisedField(self, 'OrgnlGrpId', Max35Text, False)

	@OrgnlGrpId.deleter
	def OrgnlGrpId(self):
		del self._OrgnlGrpId
		self._OrgnlGrpId = base_types.UninitialisedField(self, 'OrgnlGrpId', Max35Text, False)

	@property
	def TtlBlkInvcAmt(self):
		return self._TtlBlkInvcAmt

	@TtlBlkInvcAmt.setter
	def TtlBlkInvcAmt(self, value):
		self._TtlBlkInvcAmt = value if value is not None else base_types.UninitialisedField(self, 'TtlBlkInvcAmt', ActiveCurrencyAndAmount, False)

	@TtlBlkInvcAmt.deleter
	def TtlBlkInvcAmt(self):
		del self._TtlBlkInvcAmt
		self._TtlBlkInvcAmt = base_types.UninitialisedField(self, 'TtlBlkInvcAmt', ActiveCurrencyAndAmount, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='CxlRsn', type=Max105Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FincgRqstr', type=PartyIdentificationAndAccount6, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FrstAgt', type=FinancialInstitutionIdentification6, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='IntrmyAgt', type=FinancialInstitutionIdentification6, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NbOfInvcReqs', type=Max15NumericText, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OrgnlCreDtTm', type=ISODateTime, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OrgnlGrpId', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TtlBlkInvcAmt', type=ActiveCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
	))