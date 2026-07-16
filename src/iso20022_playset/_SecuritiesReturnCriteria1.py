# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import RequestedIndicator

class SecuritiesReturnCriteria1(base_types._BaseFieldType):

	__slots__ = ["_CSD", "_ClssfctnFinInstrm", "_CtryOfIsse", "_DevtgSttlmUnit", "_FinInstrmId", "_ISOSctyLngNm", "_ISOSctyShrtNm", "_InvstrCSD", "_IsseCcy", "_IsseDt", "_IssrCSD", "_MinDnmtn", "_MinMltplQty", "_MtrtyDt", "_SctiesQtyTp", "_SctySts", "_TechIssrCSD"]
	@property
	def CSD(self):
		return self._CSD

	@CSD.setter
	def CSD(self, value):
		self._CSD = value if value is not None else base_types.UninitialisedField(self, 'CSD', RequestedIndicator, False)

	@CSD.deleter
	def CSD(self):
		del self._CSD
		self._CSD = base_types.UninitialisedField(self, 'CSD', RequestedIndicator, False)

	@property
	def ClssfctnFinInstrm(self):
		return self._ClssfctnFinInstrm

	@ClssfctnFinInstrm.setter
	def ClssfctnFinInstrm(self, value):
		self._ClssfctnFinInstrm = value if value is not None else base_types.UninitialisedField(self, 'ClssfctnFinInstrm', RequestedIndicator, False)

	@ClssfctnFinInstrm.deleter
	def ClssfctnFinInstrm(self):
		del self._ClssfctnFinInstrm
		self._ClssfctnFinInstrm = base_types.UninitialisedField(self, 'ClssfctnFinInstrm', RequestedIndicator, False)

	@property
	def CtryOfIsse(self):
		return self._CtryOfIsse

	@CtryOfIsse.setter
	def CtryOfIsse(self, value):
		self._CtryOfIsse = value if value is not None else base_types.UninitialisedField(self, 'CtryOfIsse', RequestedIndicator, False)

	@CtryOfIsse.deleter
	def CtryOfIsse(self):
		del self._CtryOfIsse
		self._CtryOfIsse = base_types.UninitialisedField(self, 'CtryOfIsse', RequestedIndicator, False)

	@property
	def DevtgSttlmUnit(self):
		return self._DevtgSttlmUnit

	@DevtgSttlmUnit.setter
	def DevtgSttlmUnit(self, value):
		self._DevtgSttlmUnit = value if value is not None else base_types.UninitialisedField(self, 'DevtgSttlmUnit', RequestedIndicator, False)

	@DevtgSttlmUnit.deleter
	def DevtgSttlmUnit(self):
		del self._DevtgSttlmUnit
		self._DevtgSttlmUnit = base_types.UninitialisedField(self, 'DevtgSttlmUnit', RequestedIndicator, False)

	@property
	def FinInstrmId(self):
		return self._FinInstrmId

	@FinInstrmId.setter
	def FinInstrmId(self, value):
		self._FinInstrmId = value if value is not None else base_types.UninitialisedField(self, 'FinInstrmId', RequestedIndicator, False)

	@FinInstrmId.deleter
	def FinInstrmId(self):
		del self._FinInstrmId
		self._FinInstrmId = base_types.UninitialisedField(self, 'FinInstrmId', RequestedIndicator, False)

	@property
	def ISOSctyLngNm(self):
		return self._ISOSctyLngNm

	@ISOSctyLngNm.setter
	def ISOSctyLngNm(self, value):
		self._ISOSctyLngNm = value if value is not None else base_types.UninitialisedField(self, 'ISOSctyLngNm', RequestedIndicator, False)

	@ISOSctyLngNm.deleter
	def ISOSctyLngNm(self):
		del self._ISOSctyLngNm
		self._ISOSctyLngNm = base_types.UninitialisedField(self, 'ISOSctyLngNm', RequestedIndicator, False)

	@property
	def ISOSctyShrtNm(self):
		return self._ISOSctyShrtNm

	@ISOSctyShrtNm.setter
	def ISOSctyShrtNm(self, value):
		self._ISOSctyShrtNm = value if value is not None else base_types.UninitialisedField(self, 'ISOSctyShrtNm', RequestedIndicator, False)

	@ISOSctyShrtNm.deleter
	def ISOSctyShrtNm(self):
		del self._ISOSctyShrtNm
		self._ISOSctyShrtNm = base_types.UninitialisedField(self, 'ISOSctyShrtNm', RequestedIndicator, False)

	@property
	def InvstrCSD(self):
		return self._InvstrCSD

	@InvstrCSD.setter
	def InvstrCSD(self, value):
		self._InvstrCSD = value if value is not None else base_types.UninitialisedField(self, 'InvstrCSD', RequestedIndicator, False)

	@InvstrCSD.deleter
	def InvstrCSD(self):
		del self._InvstrCSD
		self._InvstrCSD = base_types.UninitialisedField(self, 'InvstrCSD', RequestedIndicator, False)

	@property
	def IsseCcy(self):
		return self._IsseCcy

	@IsseCcy.setter
	def IsseCcy(self, value):
		self._IsseCcy = value if value is not None else base_types.UninitialisedField(self, 'IsseCcy', RequestedIndicator, False)

	@IsseCcy.deleter
	def IsseCcy(self):
		del self._IsseCcy
		self._IsseCcy = base_types.UninitialisedField(self, 'IsseCcy', RequestedIndicator, False)

	@property
	def IsseDt(self):
		return self._IsseDt

	@IsseDt.setter
	def IsseDt(self, value):
		self._IsseDt = value if value is not None else base_types.UninitialisedField(self, 'IsseDt', RequestedIndicator, False)

	@IsseDt.deleter
	def IsseDt(self):
		del self._IsseDt
		self._IsseDt = base_types.UninitialisedField(self, 'IsseDt', RequestedIndicator, False)

	@property
	def IssrCSD(self):
		return self._IssrCSD

	@IssrCSD.setter
	def IssrCSD(self, value):
		self._IssrCSD = value if value is not None else base_types.UninitialisedField(self, 'IssrCSD', RequestedIndicator, False)

	@IssrCSD.deleter
	def IssrCSD(self):
		del self._IssrCSD
		self._IssrCSD = base_types.UninitialisedField(self, 'IssrCSD', RequestedIndicator, False)

	@property
	def MinDnmtn(self):
		return self._MinDnmtn

	@MinDnmtn.setter
	def MinDnmtn(self, value):
		self._MinDnmtn = value if value is not None else base_types.UninitialisedField(self, 'MinDnmtn', RequestedIndicator, False)

	@MinDnmtn.deleter
	def MinDnmtn(self):
		del self._MinDnmtn
		self._MinDnmtn = base_types.UninitialisedField(self, 'MinDnmtn', RequestedIndicator, False)

	@property
	def MinMltplQty(self):
		return self._MinMltplQty

	@MinMltplQty.setter
	def MinMltplQty(self, value):
		self._MinMltplQty = value if value is not None else base_types.UninitialisedField(self, 'MinMltplQty', RequestedIndicator, False)

	@MinMltplQty.deleter
	def MinMltplQty(self):
		del self._MinMltplQty
		self._MinMltplQty = base_types.UninitialisedField(self, 'MinMltplQty', RequestedIndicator, False)

	@property
	def MtrtyDt(self):
		return self._MtrtyDt

	@MtrtyDt.setter
	def MtrtyDt(self, value):
		self._MtrtyDt = value if value is not None else base_types.UninitialisedField(self, 'MtrtyDt', RequestedIndicator, False)

	@MtrtyDt.deleter
	def MtrtyDt(self):
		del self._MtrtyDt
		self._MtrtyDt = base_types.UninitialisedField(self, 'MtrtyDt', RequestedIndicator, False)

	@property
	def SctiesQtyTp(self):
		return self._SctiesQtyTp

	@SctiesQtyTp.setter
	def SctiesQtyTp(self, value):
		self._SctiesQtyTp = value if value is not None else base_types.UninitialisedField(self, 'SctiesQtyTp', RequestedIndicator, False)

	@SctiesQtyTp.deleter
	def SctiesQtyTp(self):
		del self._SctiesQtyTp
		self._SctiesQtyTp = base_types.UninitialisedField(self, 'SctiesQtyTp', RequestedIndicator, False)

	@property
	def SctySts(self):
		return self._SctySts

	@SctySts.setter
	def SctySts(self, value):
		self._SctySts = value if value is not None else base_types.UninitialisedField(self, 'SctySts', RequestedIndicator, False)

	@SctySts.deleter
	def SctySts(self):
		del self._SctySts
		self._SctySts = base_types.UninitialisedField(self, 'SctySts', RequestedIndicator, False)

	@property
	def TechIssrCSD(self):
		return self._TechIssrCSD

	@TechIssrCSD.setter
	def TechIssrCSD(self, value):
		self._TechIssrCSD = value if value is not None else base_types.UninitialisedField(self, 'TechIssrCSD', RequestedIndicator, False)

	@TechIssrCSD.deleter
	def TechIssrCSD(self):
		del self._TechIssrCSD
		self._TechIssrCSD = base_types.UninitialisedField(self, 'TechIssrCSD', RequestedIndicator, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='CSD', type=RequestedIndicator, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ClssfctnFinInstrm', type=RequestedIndicator, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CtryOfIsse', type=RequestedIndicator, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DevtgSttlmUnit', type=RequestedIndicator, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FinInstrmId', type=RequestedIndicator, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ISOSctyLngNm', type=RequestedIndicator, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ISOSctyShrtNm', type=RequestedIndicator, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='InvstrCSD', type=RequestedIndicator, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='IsseCcy', type=RequestedIndicator, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='IsseDt', type=RequestedIndicator, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='IssrCSD', type=RequestedIndicator, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MinDnmtn', type=RequestedIndicator, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MinMltplQty', type=RequestedIndicator, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MtrtyDt', type=RequestedIndicator, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SctiesQtyTp', type=RequestedIndicator, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SctySts', type=RequestedIndicator, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TechIssrCSD', type=RequestedIndicator, min=1, max=1, mutex_group=None, array=False),
	))