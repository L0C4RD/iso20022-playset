# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import CustomerReference1
from . import ImpliedCurrencyAndAmount
from . import Max10NumericText
from . import Max35Text
from . import Max70Text
from . import TrueFalseIndicator

class TravelAgencyPackage2(base_types._BaseFieldType):

	__slots__ = ["_CdtCardSlipNb", "_CstmrRef", "_DataSrc", "_DlvryOrdrNb", "_Fee", "_Insrnc", "_InsrncAmt", "_NbInPty", "_RsvatnNb", "_Tp"]
	@property
	def CdtCardSlipNb(self):
		return self._CdtCardSlipNb

	@CdtCardSlipNb.setter
	def CdtCardSlipNb(self, value):
		self._CdtCardSlipNb = value if value is not None else base_types.UninitialisedField(self, 'CdtCardSlipNb', Max35Text, False)

	@CdtCardSlipNb.deleter
	def CdtCardSlipNb(self):
		del self._CdtCardSlipNb
		self._CdtCardSlipNb = base_types.UninitialisedField(self, 'CdtCardSlipNb', Max35Text, False)

	@property
	def CstmrRef(self):
		return self._CstmrRef

	@CstmrRef.setter
	def CstmrRef(self, value):
		self._CstmrRef = value if value is not None else base_types.UninitialisedField(self, 'CstmrRef', CustomerReference1, True)

	@CstmrRef.deleter
	def CstmrRef(self):
		del self._CstmrRef
		self._CstmrRef = base_types.UninitialisedField(self, 'CstmrRef', CustomerReference1, True)

	@property
	def DataSrc(self):
		return self._DataSrc

	@DataSrc.setter
	def DataSrc(self, value):
		self._DataSrc = value if value is not None else base_types.UninitialisedField(self, 'DataSrc', Max35Text, False)

	@DataSrc.deleter
	def DataSrc(self):
		del self._DataSrc
		self._DataSrc = base_types.UninitialisedField(self, 'DataSrc', Max35Text, False)

	@property
	def DlvryOrdrNb(self):
		return self._DlvryOrdrNb

	@DlvryOrdrNb.setter
	def DlvryOrdrNb(self, value):
		self._DlvryOrdrNb = value if value is not None else base_types.UninitialisedField(self, 'DlvryOrdrNb', Max35Text, False)

	@DlvryOrdrNb.deleter
	def DlvryOrdrNb(self):
		del self._DlvryOrdrNb
		self._DlvryOrdrNb = base_types.UninitialisedField(self, 'DlvryOrdrNb', Max35Text, False)

	@property
	def Fee(self):
		return self._Fee

	@Fee.setter
	def Fee(self, value):
		self._Fee = value if value is not None else base_types.UninitialisedField(self, 'Fee', ImpliedCurrencyAndAmount, False)

	@Fee.deleter
	def Fee(self):
		del self._Fee
		self._Fee = base_types.UninitialisedField(self, 'Fee', ImpliedCurrencyAndAmount, False)

	@property
	def Insrnc(self):
		return self._Insrnc

	@Insrnc.setter
	def Insrnc(self, value):
		self._Insrnc = value if value is not None else base_types.UninitialisedField(self, 'Insrnc', TrueFalseIndicator, False)

	@Insrnc.deleter
	def Insrnc(self):
		del self._Insrnc
		self._Insrnc = base_types.UninitialisedField(self, 'Insrnc', TrueFalseIndicator, False)

	@property
	def InsrncAmt(self):
		return self._InsrncAmt

	@InsrncAmt.setter
	def InsrncAmt(self, value):
		self._InsrncAmt = value if value is not None else base_types.UninitialisedField(self, 'InsrncAmt', ImpliedCurrencyAndAmount, False)

	@InsrncAmt.deleter
	def InsrncAmt(self):
		del self._InsrncAmt
		self._InsrncAmt = base_types.UninitialisedField(self, 'InsrncAmt', ImpliedCurrencyAndAmount, False)

	@property
	def NbInPty(self):
		return self._NbInPty

	@NbInPty.setter
	def NbInPty(self, value):
		self._NbInPty = value if value is not None else base_types.UninitialisedField(self, 'NbInPty', Max10NumericText, False)

	@NbInPty.deleter
	def NbInPty(self):
		del self._NbInPty
		self._NbInPty = base_types.UninitialisedField(self, 'NbInPty', Max10NumericText, False)

	@property
	def RsvatnNb(self):
		return self._RsvatnNb

	@RsvatnNb.setter
	def RsvatnNb(self, value):
		self._RsvatnNb = value if value is not None else base_types.UninitialisedField(self, 'RsvatnNb', Max35Text, False)

	@RsvatnNb.deleter
	def RsvatnNb(self):
		del self._RsvatnNb
		self._RsvatnNb = base_types.UninitialisedField(self, 'RsvatnNb', Max35Text, False)

	@property
	def Tp(self):
		return self._Tp

	@Tp.setter
	def Tp(self, value):
		self._Tp = value if value is not None else base_types.UninitialisedField(self, 'Tp', Max70Text, False)

	@Tp.deleter
	def Tp(self):
		del self._Tp
		self._Tp = base_types.UninitialisedField(self, 'Tp', Max70Text, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='CdtCardSlipNb', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CstmrRef', type=CustomerReference1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='DataSrc', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DlvryOrdrNb', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Fee', type=ImpliedCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Insrnc', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='InsrncAmt', type=ImpliedCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NbInPty', type=Max10NumericText, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RsvatnNb', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Tp', type=Max70Text, min=0, max=1, mutex_group=None, array=False),
	))