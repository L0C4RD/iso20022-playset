from . import base_types
from .YesNoIndicator import YesNoIndicator

class CorporateActionSupplementaryIndicators1(base_types._BaseFieldType):

	__slots__ = ["_EscrwToMtrtyInd", "_SrrndrShrsToAgtInd", "_RghtsRndUpPrvlgInd", "_CondlPmtAplblInd", "_RghtsOvrsbcptInd", "_StepUpPrvlgInd", "_SlctnDealrFeeInd", "_RghtsTrfblInd"]
	@property
	def EscrwToMtrtyInd(self):
		return self._EscrwToMtrtyInd

	@EscrwToMtrtyInd.setter
	def EscrwToMtrtyInd(self, value):
		self._EscrwToMtrtyInd = value if type(value) != base_types.auto else self.make_default("EscrwToMtrtyInd")

	@EscrwToMtrtyInd.deleter
	def EscrwToMtrtyInd(self):
		del self._EscrwToMtrtyInd
		self._EscrwToMtrtyInd = None

	@property
	def SrrndrShrsToAgtInd(self):
		return self._SrrndrShrsToAgtInd

	@SrrndrShrsToAgtInd.setter
	def SrrndrShrsToAgtInd(self, value):
		self._SrrndrShrsToAgtInd = value if type(value) != base_types.auto else self.make_default("SrrndrShrsToAgtInd")

	@SrrndrShrsToAgtInd.deleter
	def SrrndrShrsToAgtInd(self):
		del self._SrrndrShrsToAgtInd
		self._SrrndrShrsToAgtInd = None

	@property
	def RghtsRndUpPrvlgInd(self):
		return self._RghtsRndUpPrvlgInd

	@RghtsRndUpPrvlgInd.setter
	def RghtsRndUpPrvlgInd(self, value):
		self._RghtsRndUpPrvlgInd = value if type(value) != base_types.auto else self.make_default("RghtsRndUpPrvlgInd")

	@RghtsRndUpPrvlgInd.deleter
	def RghtsRndUpPrvlgInd(self):
		del self._RghtsRndUpPrvlgInd
		self._RghtsRndUpPrvlgInd = None

	@property
	def CondlPmtAplblInd(self):
		return self._CondlPmtAplblInd

	@CondlPmtAplblInd.setter
	def CondlPmtAplblInd(self, value):
		self._CondlPmtAplblInd = value if type(value) != base_types.auto else self.make_default("CondlPmtAplblInd")

	@CondlPmtAplblInd.deleter
	def CondlPmtAplblInd(self):
		del self._CondlPmtAplblInd
		self._CondlPmtAplblInd = None

	@property
	def RghtsOvrsbcptInd(self):
		return self._RghtsOvrsbcptInd

	@RghtsOvrsbcptInd.setter
	def RghtsOvrsbcptInd(self, value):
		self._RghtsOvrsbcptInd = value if type(value) != base_types.auto else self.make_default("RghtsOvrsbcptInd")

	@RghtsOvrsbcptInd.deleter
	def RghtsOvrsbcptInd(self):
		del self._RghtsOvrsbcptInd
		self._RghtsOvrsbcptInd = None

	@property
	def StepUpPrvlgInd(self):
		return self._StepUpPrvlgInd

	@StepUpPrvlgInd.setter
	def StepUpPrvlgInd(self, value):
		self._StepUpPrvlgInd = value if type(value) != base_types.auto else self.make_default("StepUpPrvlgInd")

	@StepUpPrvlgInd.deleter
	def StepUpPrvlgInd(self):
		del self._StepUpPrvlgInd
		self._StepUpPrvlgInd = None

	@property
	def SlctnDealrFeeInd(self):
		return self._SlctnDealrFeeInd

	@SlctnDealrFeeInd.setter
	def SlctnDealrFeeInd(self, value):
		self._SlctnDealrFeeInd = value if type(value) != base_types.auto else self.make_default("SlctnDealrFeeInd")

	@SlctnDealrFeeInd.deleter
	def SlctnDealrFeeInd(self):
		del self._SlctnDealrFeeInd
		self._SlctnDealrFeeInd = None

	@property
	def RghtsTrfblInd(self):
		return self._RghtsTrfblInd

	@RghtsTrfblInd.setter
	def RghtsTrfblInd(self, value):
		self._RghtsTrfblInd = value if type(value) != base_types.auto else self.make_default("RghtsTrfblInd")

	@RghtsTrfblInd.deleter
	def RghtsTrfblInd(self):
		del self._RghtsTrfblInd
		self._RghtsTrfblInd = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='EscrwToMtrtyInd', type=YesNoIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SrrndrShrsToAgtInd', type=YesNoIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RghtsRndUpPrvlgInd', type=YesNoIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CondlPmtAplblInd', type=YesNoIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RghtsOvrsbcptInd', type=YesNoIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='StepUpPrvlgInd', type=YesNoIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SlctnDealrFeeInd', type=YesNoIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RghtsTrfblInd', type=YesNoIndicator, min=0, max=1, mutex_group=None, array=False),
	))

