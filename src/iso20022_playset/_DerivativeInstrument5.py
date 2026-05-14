# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._AssetClass2 import AssetClass2
from ._FinancialInstrumentIdentification5Choice import FinancialInstrumentIdentification5Choice
from ._ISODate import ISODate
from ._NonNegativeDecimalNumber import NonNegativeDecimalNumber
from ._OptionStyle7Code import OptionStyle7Code
from ._OptionType2Code import OptionType2Code
from ._PhysicalTransferType4Code import PhysicalTransferType4Code
from ._SecuritiesTransactionPrice4Choice import SecuritiesTransactionPrice4Choice

class DerivativeInstrument5(base_types._BaseFieldType):

	__slots__ = ["_AsstClssSpcfcAttrbts", "_DlvryTp", "_OptnExrcStyle", "_OptnTp", "_PricMltplr", "_StrkPric", "_UndrlygInstrm", "_XpryDt"]
	@property
	def AsstClssSpcfcAttrbts(self):
		return self._AsstClssSpcfcAttrbts

	@AsstClssSpcfcAttrbts.setter
	def AsstClssSpcfcAttrbts(self, value):
		self._AsstClssSpcfcAttrbts = value if type(value) != base_types.auto else self.make_default("AsstClssSpcfcAttrbts")

	@AsstClssSpcfcAttrbts.deleter
	def AsstClssSpcfcAttrbts(self):
		del self._AsstClssSpcfcAttrbts
		self._AsstClssSpcfcAttrbts = None

	@property
	def DlvryTp(self):
		return self._DlvryTp

	@DlvryTp.setter
	def DlvryTp(self, value):
		self._DlvryTp = value if type(value) != base_types.auto else self.make_default("DlvryTp")

	@DlvryTp.deleter
	def DlvryTp(self):
		del self._DlvryTp
		self._DlvryTp = None

	@property
	def OptnExrcStyle(self):
		return self._OptnExrcStyle

	@OptnExrcStyle.setter
	def OptnExrcStyle(self, value):
		self._OptnExrcStyle = value if type(value) != base_types.auto else self.make_default("OptnExrcStyle")

	@OptnExrcStyle.deleter
	def OptnExrcStyle(self):
		del self._OptnExrcStyle
		self._OptnExrcStyle = None

	@property
	def OptnTp(self):
		return self._OptnTp

	@OptnTp.setter
	def OptnTp(self, value):
		self._OptnTp = value if type(value) != base_types.auto else self.make_default("OptnTp")

	@OptnTp.deleter
	def OptnTp(self):
		del self._OptnTp
		self._OptnTp = None

	@property
	def PricMltplr(self):
		return self._PricMltplr

	@PricMltplr.setter
	def PricMltplr(self, value):
		self._PricMltplr = value if type(value) != base_types.auto else self.make_default("PricMltplr")

	@PricMltplr.deleter
	def PricMltplr(self):
		del self._PricMltplr
		self._PricMltplr = None

	@property
	def StrkPric(self):
		return self._StrkPric

	@StrkPric.setter
	def StrkPric(self, value):
		self._StrkPric = value if type(value) != base_types.auto else self.make_default("StrkPric")

	@StrkPric.deleter
	def StrkPric(self):
		del self._StrkPric
		self._StrkPric = None

	@property
	def UndrlygInstrm(self):
		return self._UndrlygInstrm

	@UndrlygInstrm.setter
	def UndrlygInstrm(self, value):
		self._UndrlygInstrm = value if type(value) != base_types.auto else self.make_default("UndrlygInstrm")

	@UndrlygInstrm.deleter
	def UndrlygInstrm(self):
		del self._UndrlygInstrm
		self._UndrlygInstrm = None

	@property
	def XpryDt(self):
		return self._XpryDt

	@XpryDt.setter
	def XpryDt(self, value):
		self._XpryDt = value if type(value) != base_types.auto else self.make_default("XpryDt")

	@XpryDt.deleter
	def XpryDt(self):
		del self._XpryDt
		self._XpryDt = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='AsstClssSpcfcAttrbts', type=AssetClass2, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DlvryTp', type=PhysicalTransferType4Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OptnExrcStyle', type=OptionStyle7Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OptnTp', type=OptionType2Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PricMltplr', type=NonNegativeDecimalNumber, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='StrkPric', type=SecuritiesTransactionPrice4Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='UndrlygInstrm', type=FinancialInstrumentIdentification5Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='XpryDt', type=ISODate, min=0, max=1, mutex_group=None, array=False),
	))