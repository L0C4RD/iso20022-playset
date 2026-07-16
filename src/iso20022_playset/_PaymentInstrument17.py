# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ActiveCurrencyCode
from . import PaymentInstrument19Choice
from . import PaymentInstrument24Choice
from . import PercentageBoundedRate

class PaymentInstrument17(base_types._BaseFieldType):

	__slots__ = ["_DvddPctg", "_DvddPmtInstrm", "_IntrstPmtInstrm", "_RedPmtInstrm", "_SbcptPmtInstrm", "_SttlmCcy", "_SvgsPlanPmtInstrm"]
	@property
	def DvddPctg(self):
		return self._DvddPctg

	@DvddPctg.setter
	def DvddPctg(self, value):
		self._DvddPctg = value if value is not None else base_types.UninitialisedField(self, 'DvddPctg', PercentageBoundedRate, False)

	@DvddPctg.deleter
	def DvddPctg(self):
		del self._DvddPctg
		self._DvddPctg = base_types.UninitialisedField(self, 'DvddPctg', PercentageBoundedRate, False)

	@property
	def DvddPmtInstrm(self):
		return self._DvddPmtInstrm

	@DvddPmtInstrm.setter
	def DvddPmtInstrm(self, value):
		self._DvddPmtInstrm = value if value is not None else base_types.UninitialisedField(self, 'DvddPmtInstrm', PaymentInstrument19Choice, False)

	@DvddPmtInstrm.deleter
	def DvddPmtInstrm(self):
		del self._DvddPmtInstrm
		self._DvddPmtInstrm = base_types.UninitialisedField(self, 'DvddPmtInstrm', PaymentInstrument19Choice, False)

	@property
	def IntrstPmtInstrm(self):
		return self._IntrstPmtInstrm

	@IntrstPmtInstrm.setter
	def IntrstPmtInstrm(self, value):
		self._IntrstPmtInstrm = value if value is not None else base_types.UninitialisedField(self, 'IntrstPmtInstrm', PaymentInstrument19Choice, False)

	@IntrstPmtInstrm.deleter
	def IntrstPmtInstrm(self):
		del self._IntrstPmtInstrm
		self._IntrstPmtInstrm = base_types.UninitialisedField(self, 'IntrstPmtInstrm', PaymentInstrument19Choice, False)

	@property
	def RedPmtInstrm(self):
		return self._RedPmtInstrm

	@RedPmtInstrm.setter
	def RedPmtInstrm(self, value):
		self._RedPmtInstrm = value if value is not None else base_types.UninitialisedField(self, 'RedPmtInstrm', PaymentInstrument19Choice, False)

	@RedPmtInstrm.deleter
	def RedPmtInstrm(self):
		del self._RedPmtInstrm
		self._RedPmtInstrm = base_types.UninitialisedField(self, 'RedPmtInstrm', PaymentInstrument19Choice, False)

	@property
	def SbcptPmtInstrm(self):
		return self._SbcptPmtInstrm

	@SbcptPmtInstrm.setter
	def SbcptPmtInstrm(self, value):
		self._SbcptPmtInstrm = value if value is not None else base_types.UninitialisedField(self, 'SbcptPmtInstrm', PaymentInstrument24Choice, False)

	@SbcptPmtInstrm.deleter
	def SbcptPmtInstrm(self):
		del self._SbcptPmtInstrm
		self._SbcptPmtInstrm = base_types.UninitialisedField(self, 'SbcptPmtInstrm', PaymentInstrument24Choice, False)

	@property
	def SttlmCcy(self):
		return self._SttlmCcy

	@SttlmCcy.setter
	def SttlmCcy(self, value):
		self._SttlmCcy = value if value is not None else base_types.UninitialisedField(self, 'SttlmCcy', ActiveCurrencyCode, False)

	@SttlmCcy.deleter
	def SttlmCcy(self):
		del self._SttlmCcy
		self._SttlmCcy = base_types.UninitialisedField(self, 'SttlmCcy', ActiveCurrencyCode, False)

	@property
	def SvgsPlanPmtInstrm(self):
		return self._SvgsPlanPmtInstrm

	@SvgsPlanPmtInstrm.setter
	def SvgsPlanPmtInstrm(self, value):
		self._SvgsPlanPmtInstrm = value if value is not None else base_types.UninitialisedField(self, 'SvgsPlanPmtInstrm', PaymentInstrument24Choice, False)

	@SvgsPlanPmtInstrm.deleter
	def SvgsPlanPmtInstrm(self):
		del self._SvgsPlanPmtInstrm
		self._SvgsPlanPmtInstrm = base_types.UninitialisedField(self, 'SvgsPlanPmtInstrm', PaymentInstrument24Choice, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='DvddPctg', type=PercentageBoundedRate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DvddPmtInstrm', type=PaymentInstrument19Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='IntrstPmtInstrm', type=PaymentInstrument19Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RedPmtInstrm', type=PaymentInstrument19Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SbcptPmtInstrm', type=PaymentInstrument24Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SttlmCcy', type=ActiveCurrencyCode, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SvgsPlanPmtInstrm', type=PaymentInstrument24Choice, min=0, max=1, mutex_group=None, array=False),
	))