import base_types
import Max70Text
import ImpliedCurrencyAndAmount
import CustomerReference1
import Max10NumericText
import Max35Text
import TrueFalseIndicator

class TravelAgencyPackage2(base_types._BaseFieldType):

	__slots__ = ["_NbInPty", "_InsrncAmt", "_RsvatnNb", "_Fee", "_Tp", "_DlvryOrdrNb", "_Insrnc", "_CdtCardSlipNb", "_CstmrRef", "_DataSrc"]
	@property
	def NbInPty(self):
		return self._NbInPty

	@NbInPty.setter
	def NbInPty(self, value):
		self._NbInPty = value if type(value) != auto else self.make_default("NbInPty")

	@NbInPty.deleter
	def NbInPty(self):
		del self._NbInPty
		self._NbInPty = None

	@property
	def InsrncAmt(self):
		return self._InsrncAmt

	@InsrncAmt.setter
	def InsrncAmt(self, value):
		self._InsrncAmt = value if type(value) != auto else self.make_default("InsrncAmt")

	@InsrncAmt.deleter
	def InsrncAmt(self):
		del self._InsrncAmt
		self._InsrncAmt = None

	@property
	def RsvatnNb(self):
		return self._RsvatnNb

	@RsvatnNb.setter
	def RsvatnNb(self, value):
		self._RsvatnNb = value if type(value) != auto else self.make_default("RsvatnNb")

	@RsvatnNb.deleter
	def RsvatnNb(self):
		del self._RsvatnNb
		self._RsvatnNb = None

	@property
	def Fee(self):
		return self._Fee

	@Fee.setter
	def Fee(self, value):
		self._Fee = value if type(value) != auto else self.make_default("Fee")

	@Fee.deleter
	def Fee(self):
		del self._Fee
		self._Fee = None

	@property
	def Tp(self):
		return self._Tp

	@Tp.setter
	def Tp(self, value):
		self._Tp = value if type(value) != auto else self.make_default("Tp")

	@Tp.deleter
	def Tp(self):
		del self._Tp
		self._Tp = None

	@property
	def DlvryOrdrNb(self):
		return self._DlvryOrdrNb

	@DlvryOrdrNb.setter
	def DlvryOrdrNb(self, value):
		self._DlvryOrdrNb = value if type(value) != auto else self.make_default("DlvryOrdrNb")

	@DlvryOrdrNb.deleter
	def DlvryOrdrNb(self):
		del self._DlvryOrdrNb
		self._DlvryOrdrNb = None

	@property
	def Insrnc(self):
		return self._Insrnc

	@Insrnc.setter
	def Insrnc(self, value):
		self._Insrnc = value if type(value) != auto else self.make_default("Insrnc")

	@Insrnc.deleter
	def Insrnc(self):
		del self._Insrnc
		self._Insrnc = None

	@property
	def CdtCardSlipNb(self):
		return self._CdtCardSlipNb

	@CdtCardSlipNb.setter
	def CdtCardSlipNb(self, value):
		self._CdtCardSlipNb = value if type(value) != auto else self.make_default("CdtCardSlipNb")

	@CdtCardSlipNb.deleter
	def CdtCardSlipNb(self):
		del self._CdtCardSlipNb
		self._CdtCardSlipNb = None

	@property
	def CstmrRef(self):
		return self._CstmrRef

	@CstmrRef.setter
	def CstmrRef(self, value):
		self._CstmrRef = value if type(value) != auto else self.make_default("CstmrRef")

	@CstmrRef.deleter
	def CstmrRef(self):
		del self._CstmrRef
		self._CstmrRef = None

	@property
	def DataSrc(self):
		return self._DataSrc

	@DataSrc.setter
	def DataSrc(self, value):
		self._DataSrc = value if type(value) != auto else self.make_default("DataSrc")

	@DataSrc.deleter
	def DataSrc(self):
		del self._DataSrc
		self._DataSrc = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='NbInPty', type=Max10NumericText, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='InsrncAmt', type=ImpliedCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RsvatnNb', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Fee', type=ImpliedCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Tp', type=Max70Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DlvryOrdrNb', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Insrnc', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CdtCardSlipNb', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CstmrRef', type=CustomerReference1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='DataSrc', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
	))

