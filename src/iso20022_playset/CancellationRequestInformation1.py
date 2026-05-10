import base_types
import PartyIdentificationAndAccount6
import Max15NumericText
import ISODateTime
import FinancialInstitutionIdentification6
import Max35Text
import Max105Text
import ActiveCurrencyAndAmount

class CancellationRequestInformation1(base_types._BaseFieldType):

	__slots__ = ["_FrstAgt", "_OrgnlGrpId", "_NbOfInvcReqs", "_IntrmyAgt", "_FincgRqstr", "_CxlRsn", "_TtlBlkInvcAmt", "_OrgnlCreDtTm"]
	@property
	def FrstAgt(self):
		return self._FrstAgt

	@FrstAgt.setter
	def FrstAgt(self, value):
		self._FrstAgt = value if type(value) != auto else self.make_default("FrstAgt")

	@FrstAgt.deleter
	def FrstAgt(self):
		del self._FrstAgt
		self._FrstAgt = None

	@property
	def OrgnlGrpId(self):
		return self._OrgnlGrpId

	@OrgnlGrpId.setter
	def OrgnlGrpId(self, value):
		self._OrgnlGrpId = value if type(value) != auto else self.make_default("OrgnlGrpId")

	@OrgnlGrpId.deleter
	def OrgnlGrpId(self):
		del self._OrgnlGrpId
		self._OrgnlGrpId = None

	@property
	def NbOfInvcReqs(self):
		return self._NbOfInvcReqs

	@NbOfInvcReqs.setter
	def NbOfInvcReqs(self, value):
		self._NbOfInvcReqs = value if type(value) != auto else self.make_default("NbOfInvcReqs")

	@NbOfInvcReqs.deleter
	def NbOfInvcReqs(self):
		del self._NbOfInvcReqs
		self._NbOfInvcReqs = None

	@property
	def IntrmyAgt(self):
		return self._IntrmyAgt

	@IntrmyAgt.setter
	def IntrmyAgt(self, value):
		self._IntrmyAgt = value if type(value) != auto else self.make_default("IntrmyAgt")

	@IntrmyAgt.deleter
	def IntrmyAgt(self):
		del self._IntrmyAgt
		self._IntrmyAgt = None

	@property
	def FincgRqstr(self):
		return self._FincgRqstr

	@FincgRqstr.setter
	def FincgRqstr(self, value):
		self._FincgRqstr = value if type(value) != auto else self.make_default("FincgRqstr")

	@FincgRqstr.deleter
	def FincgRqstr(self):
		del self._FincgRqstr
		self._FincgRqstr = None

	@property
	def CxlRsn(self):
		return self._CxlRsn

	@CxlRsn.setter
	def CxlRsn(self, value):
		self._CxlRsn = value if type(value) != auto else self.make_default("CxlRsn")

	@CxlRsn.deleter
	def CxlRsn(self):
		del self._CxlRsn
		self._CxlRsn = None

	@property
	def TtlBlkInvcAmt(self):
		return self._TtlBlkInvcAmt

	@TtlBlkInvcAmt.setter
	def TtlBlkInvcAmt(self, value):
		self._TtlBlkInvcAmt = value if type(value) != auto else self.make_default("TtlBlkInvcAmt")

	@TtlBlkInvcAmt.deleter
	def TtlBlkInvcAmt(self):
		del self._TtlBlkInvcAmt
		self._TtlBlkInvcAmt = None

	@property
	def OrgnlCreDtTm(self):
		return self._OrgnlCreDtTm

	@OrgnlCreDtTm.setter
	def OrgnlCreDtTm(self, value):
		self._OrgnlCreDtTm = value if type(value) != auto else self.make_default("OrgnlCreDtTm")

	@OrgnlCreDtTm.deleter
	def OrgnlCreDtTm(self):
		del self._OrgnlCreDtTm
		self._OrgnlCreDtTm = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='FrstAgt', type=FinancialInstitutionIdentification6, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OrgnlGrpId', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NbOfInvcReqs', type=Max15NumericText, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='IntrmyAgt', type=FinancialInstitutionIdentification6, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FincgRqstr', type=PartyIdentificationAndAccount6, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CxlRsn', type=Max105Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TtlBlkInvcAmt', type=ActiveCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OrgnlCreDtTm', type=ISODateTime, min=1, max=1, mutex_group=None, array=False),
	))

