# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import YesNoIndicator

class CorporateActionSupplementaryIndicators1(base_types._BaseFieldType):

	__slots__ = ["_CondlPmtAplblInd", "_EscrwToMtrtyInd", "_RghtsOvrsbcptInd", "_RghtsRndUpPrvlgInd", "_RghtsTrfblInd", "_SlctnDealrFeeInd", "_SrrndrShrsToAgtInd", "_StepUpPrvlgInd"]
	@property
	def CondlPmtAplblInd(self):
		return self._CondlPmtAplblInd

	@CondlPmtAplblInd.setter
	def CondlPmtAplblInd(self, value):
		self._CondlPmtAplblInd = value if value is not None else base_types.UninitialisedField(self, 'CondlPmtAplblInd', YesNoIndicator, False)

	@CondlPmtAplblInd.deleter
	def CondlPmtAplblInd(self):
		del self._CondlPmtAplblInd
		self._CondlPmtAplblInd = base_types.UninitialisedField(self, 'CondlPmtAplblInd', YesNoIndicator, False)

	@property
	def EscrwToMtrtyInd(self):
		return self._EscrwToMtrtyInd

	@EscrwToMtrtyInd.setter
	def EscrwToMtrtyInd(self, value):
		self._EscrwToMtrtyInd = value if value is not None else base_types.UninitialisedField(self, 'EscrwToMtrtyInd', YesNoIndicator, False)

	@EscrwToMtrtyInd.deleter
	def EscrwToMtrtyInd(self):
		del self._EscrwToMtrtyInd
		self._EscrwToMtrtyInd = base_types.UninitialisedField(self, 'EscrwToMtrtyInd', YesNoIndicator, False)

	@property
	def RghtsOvrsbcptInd(self):
		return self._RghtsOvrsbcptInd

	@RghtsOvrsbcptInd.setter
	def RghtsOvrsbcptInd(self, value):
		self._RghtsOvrsbcptInd = value if value is not None else base_types.UninitialisedField(self, 'RghtsOvrsbcptInd', YesNoIndicator, False)

	@RghtsOvrsbcptInd.deleter
	def RghtsOvrsbcptInd(self):
		del self._RghtsOvrsbcptInd
		self._RghtsOvrsbcptInd = base_types.UninitialisedField(self, 'RghtsOvrsbcptInd', YesNoIndicator, False)

	@property
	def RghtsRndUpPrvlgInd(self):
		return self._RghtsRndUpPrvlgInd

	@RghtsRndUpPrvlgInd.setter
	def RghtsRndUpPrvlgInd(self, value):
		self._RghtsRndUpPrvlgInd = value if value is not None else base_types.UninitialisedField(self, 'RghtsRndUpPrvlgInd', YesNoIndicator, False)

	@RghtsRndUpPrvlgInd.deleter
	def RghtsRndUpPrvlgInd(self):
		del self._RghtsRndUpPrvlgInd
		self._RghtsRndUpPrvlgInd = base_types.UninitialisedField(self, 'RghtsRndUpPrvlgInd', YesNoIndicator, False)

	@property
	def RghtsTrfblInd(self):
		return self._RghtsTrfblInd

	@RghtsTrfblInd.setter
	def RghtsTrfblInd(self, value):
		self._RghtsTrfblInd = value if value is not None else base_types.UninitialisedField(self, 'RghtsTrfblInd', YesNoIndicator, False)

	@RghtsTrfblInd.deleter
	def RghtsTrfblInd(self):
		del self._RghtsTrfblInd
		self._RghtsTrfblInd = base_types.UninitialisedField(self, 'RghtsTrfblInd', YesNoIndicator, False)

	@property
	def SlctnDealrFeeInd(self):
		return self._SlctnDealrFeeInd

	@SlctnDealrFeeInd.setter
	def SlctnDealrFeeInd(self, value):
		self._SlctnDealrFeeInd = value if value is not None else base_types.UninitialisedField(self, 'SlctnDealrFeeInd', YesNoIndicator, False)

	@SlctnDealrFeeInd.deleter
	def SlctnDealrFeeInd(self):
		del self._SlctnDealrFeeInd
		self._SlctnDealrFeeInd = base_types.UninitialisedField(self, 'SlctnDealrFeeInd', YesNoIndicator, False)

	@property
	def SrrndrShrsToAgtInd(self):
		return self._SrrndrShrsToAgtInd

	@SrrndrShrsToAgtInd.setter
	def SrrndrShrsToAgtInd(self, value):
		self._SrrndrShrsToAgtInd = value if value is not None else base_types.UninitialisedField(self, 'SrrndrShrsToAgtInd', YesNoIndicator, False)

	@SrrndrShrsToAgtInd.deleter
	def SrrndrShrsToAgtInd(self):
		del self._SrrndrShrsToAgtInd
		self._SrrndrShrsToAgtInd = base_types.UninitialisedField(self, 'SrrndrShrsToAgtInd', YesNoIndicator, False)

	@property
	def StepUpPrvlgInd(self):
		return self._StepUpPrvlgInd

	@StepUpPrvlgInd.setter
	def StepUpPrvlgInd(self, value):
		self._StepUpPrvlgInd = value if value is not None else base_types.UninitialisedField(self, 'StepUpPrvlgInd', YesNoIndicator, False)

	@StepUpPrvlgInd.deleter
	def StepUpPrvlgInd(self):
		del self._StepUpPrvlgInd
		self._StepUpPrvlgInd = base_types.UninitialisedField(self, 'StepUpPrvlgInd', YesNoIndicator, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='CondlPmtAplblInd', type=YesNoIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='EscrwToMtrtyInd', type=YesNoIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RghtsOvrsbcptInd', type=YesNoIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RghtsRndUpPrvlgInd', type=YesNoIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RghtsTrfblInd', type=YesNoIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SlctnDealrFeeInd', type=YesNoIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SrrndrShrsToAgtInd', type=YesNoIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='StepUpPrvlgInd', type=YesNoIndicator, min=0, max=1, mutex_group=None, array=False),
	))