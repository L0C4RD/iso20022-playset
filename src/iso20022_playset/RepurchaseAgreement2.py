from . import base_types
import ISODate
import RepurchaseAgreementType3Choice
import LEIIdentifier
import ActiveCurrencyAndAmount

class RepurchaseAgreement2(base_types._BaseFieldType):

	__slots__ = ["_MtrtyDt", "_RpAgrmtTp", "_CollMktVal", "_ScndLegPric", "_TrptyAgtId", "_CtrPty"]
	@property
	def MtrtyDt(self):
		return self._MtrtyDt

	@MtrtyDt.setter
	def MtrtyDt(self, value):
		self._MtrtyDt = value if type(value) != auto else self.make_default("MtrtyDt")

	@MtrtyDt.deleter
	def MtrtyDt(self):
		del self._MtrtyDt
		self._MtrtyDt = None

	@property
	def RpAgrmtTp(self):
		return self._RpAgrmtTp

	@RpAgrmtTp.setter
	def RpAgrmtTp(self, value):
		self._RpAgrmtTp = value if type(value) != auto else self.make_default("RpAgrmtTp")

	@RpAgrmtTp.deleter
	def RpAgrmtTp(self):
		del self._RpAgrmtTp
		self._RpAgrmtTp = None

	@property
	def CollMktVal(self):
		return self._CollMktVal

	@CollMktVal.setter
	def CollMktVal(self, value):
		self._CollMktVal = value if type(value) != auto else self.make_default("CollMktVal")

	@CollMktVal.deleter
	def CollMktVal(self):
		del self._CollMktVal
		self._CollMktVal = None

	@property
	def ScndLegPric(self):
		return self._ScndLegPric

	@ScndLegPric.setter
	def ScndLegPric(self, value):
		self._ScndLegPric = value if type(value) != auto else self.make_default("ScndLegPric")

	@ScndLegPric.deleter
	def ScndLegPric(self):
		del self._ScndLegPric
		self._ScndLegPric = None

	@property
	def TrptyAgtId(self):
		return self._TrptyAgtId

	@TrptyAgtId.setter
	def TrptyAgtId(self, value):
		self._TrptyAgtId = value if type(value) != auto else self.make_default("TrptyAgtId")

	@TrptyAgtId.deleter
	def TrptyAgtId(self):
		del self._TrptyAgtId
		self._TrptyAgtId = None

	@property
	def CtrPty(self):
		return self._CtrPty

	@CtrPty.setter
	def CtrPty(self, value):
		self._CtrPty = value if type(value) != auto else self.make_default("CtrPty")

	@CtrPty.deleter
	def CtrPty(self):
		del self._CtrPty
		self._CtrPty = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='MtrtyDt', type=ISODate, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RpAgrmtTp', type=RepurchaseAgreementType3Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CollMktVal', type=ActiveCurrencyAndAmount, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ScndLegPric', type=ActiveCurrencyAndAmount, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TrptyAgtId', type=LEIIdentifier, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CtrPty', type=LEIIdentifier, min=1, max=1, mutex_group=None, array=False),
	))

