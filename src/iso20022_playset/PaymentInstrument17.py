from . import base_types
import PaymentInstrument24Choice
import PaymentInstrument19Choice
import PercentageBoundedRate
import ActiveCurrencyCode

class PaymentInstrument17(base_types._BaseFieldType):

	__slots__ = ["_SvgsPlanPmtInstrm", "_SttlmCcy", "_RedPmtInstrm", "_DvddPctg", "_SbcptPmtInstrm", "_IntrstPmtInstrm", "_DvddPmtInstrm"]
	@property
	def SvgsPlanPmtInstrm(self):
		return self._SvgsPlanPmtInstrm

	@SvgsPlanPmtInstrm.setter
	def SvgsPlanPmtInstrm(self, value):
		self._SvgsPlanPmtInstrm = value if type(value) != auto else self.make_default("SvgsPlanPmtInstrm")

	@SvgsPlanPmtInstrm.deleter
	def SvgsPlanPmtInstrm(self):
		del self._SvgsPlanPmtInstrm
		self._SvgsPlanPmtInstrm = None

	@property
	def SttlmCcy(self):
		return self._SttlmCcy

	@SttlmCcy.setter
	def SttlmCcy(self, value):
		self._SttlmCcy = value if type(value) != auto else self.make_default("SttlmCcy")

	@SttlmCcy.deleter
	def SttlmCcy(self):
		del self._SttlmCcy
		self._SttlmCcy = None

	@property
	def RedPmtInstrm(self):
		return self._RedPmtInstrm

	@RedPmtInstrm.setter
	def RedPmtInstrm(self, value):
		self._RedPmtInstrm = value if type(value) != auto else self.make_default("RedPmtInstrm")

	@RedPmtInstrm.deleter
	def RedPmtInstrm(self):
		del self._RedPmtInstrm
		self._RedPmtInstrm = None

	@property
	def DvddPctg(self):
		return self._DvddPctg

	@DvddPctg.setter
	def DvddPctg(self, value):
		self._DvddPctg = value if type(value) != auto else self.make_default("DvddPctg")

	@DvddPctg.deleter
	def DvddPctg(self):
		del self._DvddPctg
		self._DvddPctg = None

	@property
	def SbcptPmtInstrm(self):
		return self._SbcptPmtInstrm

	@SbcptPmtInstrm.setter
	def SbcptPmtInstrm(self, value):
		self._SbcptPmtInstrm = value if type(value) != auto else self.make_default("SbcptPmtInstrm")

	@SbcptPmtInstrm.deleter
	def SbcptPmtInstrm(self):
		del self._SbcptPmtInstrm
		self._SbcptPmtInstrm = None

	@property
	def IntrstPmtInstrm(self):
		return self._IntrstPmtInstrm

	@IntrstPmtInstrm.setter
	def IntrstPmtInstrm(self, value):
		self._IntrstPmtInstrm = value if type(value) != auto else self.make_default("IntrstPmtInstrm")

	@IntrstPmtInstrm.deleter
	def IntrstPmtInstrm(self):
		del self._IntrstPmtInstrm
		self._IntrstPmtInstrm = None

	@property
	def DvddPmtInstrm(self):
		return self._DvddPmtInstrm

	@DvddPmtInstrm.setter
	def DvddPmtInstrm(self, value):
		self._DvddPmtInstrm = value if type(value) != auto else self.make_default("DvddPmtInstrm")

	@DvddPmtInstrm.deleter
	def DvddPmtInstrm(self):
		del self._DvddPmtInstrm
		self._DvddPmtInstrm = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='SvgsPlanPmtInstrm', type=PaymentInstrument24Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SttlmCcy', type=ActiveCurrencyCode, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RedPmtInstrm', type=PaymentInstrument19Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DvddPctg', type=PercentageBoundedRate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SbcptPmtInstrm', type=PaymentInstrument24Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='IntrstPmtInstrm', type=PaymentInstrument19Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DvddPmtInstrm', type=PaymentInstrument19Choice, min=0, max=1, mutex_group=None, array=False),
	))

