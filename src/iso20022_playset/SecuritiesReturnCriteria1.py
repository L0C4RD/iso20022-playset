import base_types
import RequestedIndicator

class SecuritiesReturnCriteria1(base_types._BaseFieldType):

	__slots__ = ["_ISOSctyShrtNm", "_CtryOfIsse", "_SctiesQtyTp", "_ISOSctyLngNm", "_CSD", "_DevtgSttlmUnit", "_TechIssrCSD", "_FinInstrmId", "_MinMltplQty", "_ClssfctnFinInstrm", "_IsseCcy", "_InvstrCSD", "_MtrtyDt", "_IsseDt", "_MinDnmtn", "_SctySts", "_IssrCSD"]
	@property
	def ISOSctyShrtNm(self):
		return self._ISOSctyShrtNm

	@ISOSctyShrtNm.setter
	def ISOSctyShrtNm(self, value):
		self._ISOSctyShrtNm = value if type(value) != auto else self.make_default("ISOSctyShrtNm")

	@ISOSctyShrtNm.deleter
	def ISOSctyShrtNm(self):
		del self._ISOSctyShrtNm
		self._ISOSctyShrtNm = None

	@property
	def CtryOfIsse(self):
		return self._CtryOfIsse

	@CtryOfIsse.setter
	def CtryOfIsse(self, value):
		self._CtryOfIsse = value if type(value) != auto else self.make_default("CtryOfIsse")

	@CtryOfIsse.deleter
	def CtryOfIsse(self):
		del self._CtryOfIsse
		self._CtryOfIsse = None

	@property
	def SctiesQtyTp(self):
		return self._SctiesQtyTp

	@SctiesQtyTp.setter
	def SctiesQtyTp(self, value):
		self._SctiesQtyTp = value if type(value) != auto else self.make_default("SctiesQtyTp")

	@SctiesQtyTp.deleter
	def SctiesQtyTp(self):
		del self._SctiesQtyTp
		self._SctiesQtyTp = None

	@property
	def ISOSctyLngNm(self):
		return self._ISOSctyLngNm

	@ISOSctyLngNm.setter
	def ISOSctyLngNm(self, value):
		self._ISOSctyLngNm = value if type(value) != auto else self.make_default("ISOSctyLngNm")

	@ISOSctyLngNm.deleter
	def ISOSctyLngNm(self):
		del self._ISOSctyLngNm
		self._ISOSctyLngNm = None

	@property
	def CSD(self):
		return self._CSD

	@CSD.setter
	def CSD(self, value):
		self._CSD = value if type(value) != auto else self.make_default("CSD")

	@CSD.deleter
	def CSD(self):
		del self._CSD
		self._CSD = None

	@property
	def DevtgSttlmUnit(self):
		return self._DevtgSttlmUnit

	@DevtgSttlmUnit.setter
	def DevtgSttlmUnit(self, value):
		self._DevtgSttlmUnit = value if type(value) != auto else self.make_default("DevtgSttlmUnit")

	@DevtgSttlmUnit.deleter
	def DevtgSttlmUnit(self):
		del self._DevtgSttlmUnit
		self._DevtgSttlmUnit = None

	@property
	def TechIssrCSD(self):
		return self._TechIssrCSD

	@TechIssrCSD.setter
	def TechIssrCSD(self, value):
		self._TechIssrCSD = value if type(value) != auto else self.make_default("TechIssrCSD")

	@TechIssrCSD.deleter
	def TechIssrCSD(self):
		del self._TechIssrCSD
		self._TechIssrCSD = None

	@property
	def FinInstrmId(self):
		return self._FinInstrmId

	@FinInstrmId.setter
	def FinInstrmId(self, value):
		self._FinInstrmId = value if type(value) != auto else self.make_default("FinInstrmId")

	@FinInstrmId.deleter
	def FinInstrmId(self):
		del self._FinInstrmId
		self._FinInstrmId = None

	@property
	def MinMltplQty(self):
		return self._MinMltplQty

	@MinMltplQty.setter
	def MinMltplQty(self, value):
		self._MinMltplQty = value if type(value) != auto else self.make_default("MinMltplQty")

	@MinMltplQty.deleter
	def MinMltplQty(self):
		del self._MinMltplQty
		self._MinMltplQty = None

	@property
	def ClssfctnFinInstrm(self):
		return self._ClssfctnFinInstrm

	@ClssfctnFinInstrm.setter
	def ClssfctnFinInstrm(self, value):
		self._ClssfctnFinInstrm = value if type(value) != auto else self.make_default("ClssfctnFinInstrm")

	@ClssfctnFinInstrm.deleter
	def ClssfctnFinInstrm(self):
		del self._ClssfctnFinInstrm
		self._ClssfctnFinInstrm = None

	@property
	def IsseCcy(self):
		return self._IsseCcy

	@IsseCcy.setter
	def IsseCcy(self, value):
		self._IsseCcy = value if type(value) != auto else self.make_default("IsseCcy")

	@IsseCcy.deleter
	def IsseCcy(self):
		del self._IsseCcy
		self._IsseCcy = None

	@property
	def InvstrCSD(self):
		return self._InvstrCSD

	@InvstrCSD.setter
	def InvstrCSD(self, value):
		self._InvstrCSD = value if type(value) != auto else self.make_default("InvstrCSD")

	@InvstrCSD.deleter
	def InvstrCSD(self):
		del self._InvstrCSD
		self._InvstrCSD = None

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
	def IsseDt(self):
		return self._IsseDt

	@IsseDt.setter
	def IsseDt(self, value):
		self._IsseDt = value if type(value) != auto else self.make_default("IsseDt")

	@IsseDt.deleter
	def IsseDt(self):
		del self._IsseDt
		self._IsseDt = None

	@property
	def MinDnmtn(self):
		return self._MinDnmtn

	@MinDnmtn.setter
	def MinDnmtn(self, value):
		self._MinDnmtn = value if type(value) != auto else self.make_default("MinDnmtn")

	@MinDnmtn.deleter
	def MinDnmtn(self):
		del self._MinDnmtn
		self._MinDnmtn = None

	@property
	def SctySts(self):
		return self._SctySts

	@SctySts.setter
	def SctySts(self, value):
		self._SctySts = value if type(value) != auto else self.make_default("SctySts")

	@SctySts.deleter
	def SctySts(self):
		del self._SctySts
		self._SctySts = None

	@property
	def IssrCSD(self):
		return self._IssrCSD

	@IssrCSD.setter
	def IssrCSD(self, value):
		self._IssrCSD = value if type(value) != auto else self.make_default("IssrCSD")

	@IssrCSD.deleter
	def IssrCSD(self):
		del self._IssrCSD
		self._IssrCSD = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='ISOSctyShrtNm', type=RequestedIndicator, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CtryOfIsse', type=RequestedIndicator, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SctiesQtyTp', type=RequestedIndicator, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ISOSctyLngNm', type=RequestedIndicator, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CSD', type=RequestedIndicator, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DevtgSttlmUnit', type=RequestedIndicator, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TechIssrCSD', type=RequestedIndicator, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FinInstrmId', type=RequestedIndicator, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MinMltplQty', type=RequestedIndicator, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ClssfctnFinInstrm', type=RequestedIndicator, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='IsseCcy', type=RequestedIndicator, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='InvstrCSD', type=RequestedIndicator, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MtrtyDt', type=RequestedIndicator, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='IsseDt', type=RequestedIndicator, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MinDnmtn', type=RequestedIndicator, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SctySts', type=RequestedIndicator, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='IssrCSD', type=RequestedIndicator, min=1, max=1, mutex_group=None, array=False),
	))

