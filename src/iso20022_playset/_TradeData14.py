from . import base_types
from ._YesNoIndicator import YesNoIndicator
from ._Status28Choice import Status28Choice
from ._Max35Text import Max35Text
from ._StatusAndSubStatus2 import StatusAndSubStatus2
from ._StatusSubType2Code import StatusSubType2Code
from ._ISODateTime import ISODateTime

class TradeData14(base_types._BaseFieldType):

	__slots__ = ["_CurSts", "_MtchgSysUnqRef", "_PrvsStsSubTp", "_MtchgSysMtchgRef", "_MtchgSysMtchdSdRef", "_PrvsSts", "_CurStsSubTp", "_StsOrgtr", "_CurStsDtTm", "_AllgdTrad"]
	@property
	def CurSts(self):
		return self._CurSts

	@CurSts.setter
	def CurSts(self, value):
		self._CurSts = value if type(value) != base_types.auto else self.make_default("CurSts")

	@CurSts.deleter
	def CurSts(self):
		del self._CurSts
		self._CurSts = None

	@property
	def MtchgSysUnqRef(self):
		return self._MtchgSysUnqRef

	@MtchgSysUnqRef.setter
	def MtchgSysUnqRef(self, value):
		self._MtchgSysUnqRef = value if type(value) != base_types.auto else self.make_default("MtchgSysUnqRef")

	@MtchgSysUnqRef.deleter
	def MtchgSysUnqRef(self):
		del self._MtchgSysUnqRef
		self._MtchgSysUnqRef = None

	@property
	def PrvsStsSubTp(self):
		return self._PrvsStsSubTp

	@PrvsStsSubTp.setter
	def PrvsStsSubTp(self, value):
		self._PrvsStsSubTp = value if type(value) != base_types.auto else self.make_default("PrvsStsSubTp")

	@PrvsStsSubTp.deleter
	def PrvsStsSubTp(self):
		del self._PrvsStsSubTp
		self._PrvsStsSubTp = None

	@property
	def MtchgSysMtchgRef(self):
		return self._MtchgSysMtchgRef

	@MtchgSysMtchgRef.setter
	def MtchgSysMtchgRef(self, value):
		self._MtchgSysMtchgRef = value if type(value) != base_types.auto else self.make_default("MtchgSysMtchgRef")

	@MtchgSysMtchgRef.deleter
	def MtchgSysMtchgRef(self):
		del self._MtchgSysMtchgRef
		self._MtchgSysMtchgRef = None

	@property
	def MtchgSysMtchdSdRef(self):
		return self._MtchgSysMtchdSdRef

	@MtchgSysMtchdSdRef.setter
	def MtchgSysMtchdSdRef(self, value):
		self._MtchgSysMtchdSdRef = value if type(value) != base_types.auto else self.make_default("MtchgSysMtchdSdRef")

	@MtchgSysMtchdSdRef.deleter
	def MtchgSysMtchdSdRef(self):
		del self._MtchgSysMtchdSdRef
		self._MtchgSysMtchdSdRef = None

	@property
	def PrvsSts(self):
		return self._PrvsSts

	@PrvsSts.setter
	def PrvsSts(self, value):
		self._PrvsSts = value if type(value) != base_types.auto else self.make_default("PrvsSts")

	@PrvsSts.deleter
	def PrvsSts(self):
		del self._PrvsSts
		self._PrvsSts = None

	@property
	def CurStsSubTp(self):
		return self._CurStsSubTp

	@CurStsSubTp.setter
	def CurStsSubTp(self, value):
		self._CurStsSubTp = value if type(value) != base_types.auto else self.make_default("CurStsSubTp")

	@CurStsSubTp.deleter
	def CurStsSubTp(self):
		del self._CurStsSubTp
		self._CurStsSubTp = None

	@property
	def StsOrgtr(self):
		return self._StsOrgtr

	@StsOrgtr.setter
	def StsOrgtr(self, value):
		self._StsOrgtr = value if type(value) != base_types.auto else self.make_default("StsOrgtr")

	@StsOrgtr.deleter
	def StsOrgtr(self):
		del self._StsOrgtr
		self._StsOrgtr = None

	@property
	def CurStsDtTm(self):
		return self._CurStsDtTm

	@CurStsDtTm.setter
	def CurStsDtTm(self, value):
		self._CurStsDtTm = value if type(value) != base_types.auto else self.make_default("CurStsDtTm")

	@CurStsDtTm.deleter
	def CurStsDtTm(self):
		del self._CurStsDtTm
		self._CurStsDtTm = None

	@property
	def AllgdTrad(self):
		return self._AllgdTrad

	@AllgdTrad.setter
	def AllgdTrad(self, value):
		self._AllgdTrad = value if type(value) != base_types.auto else self.make_default("AllgdTrad")

	@AllgdTrad.deleter
	def AllgdTrad(self):
		del self._AllgdTrad
		self._AllgdTrad = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='CurSts', type=StatusAndSubStatus2, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MtchgSysUnqRef', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrvsStsSubTp', type=StatusSubType2Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MtchgSysMtchgRef', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MtchgSysMtchdSdRef', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrvsSts', type=Status28Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CurStsSubTp', type=StatusSubType2Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='StsOrgtr', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CurStsDtTm', type=ISODateTime, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AllgdTrad', type=YesNoIndicator, min=0, max=1, mutex_group=None, array=False),
	))

