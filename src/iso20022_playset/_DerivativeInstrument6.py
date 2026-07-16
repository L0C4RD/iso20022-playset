# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import AssetClassAttributes1Choice
from . import ISODate
from . import NonNegativeDecimalNumber
from . import OptionStyle7Code
from . import OptionType2Code
from . import PhysicalTransferType4Code
from . import SecuritiesTransactionPrice4Choice
from . import UnderlyingIdentification2Choice

class DerivativeInstrument6(base_types._BaseFieldType):

	__slots__ = ["_AsstClssSpcfcAttrbts", "_DlvryTp", "_OptnExrcStyle", "_OptnTp", "_PricMltplr", "_StrkPric", "_UndrlygInstrm", "_XpryDt"]
	@property
	def AsstClssSpcfcAttrbts(self):
		return self._AsstClssSpcfcAttrbts

	@AsstClssSpcfcAttrbts.setter
	def AsstClssSpcfcAttrbts(self, value):
		self._AsstClssSpcfcAttrbts = value if value is not None else base_types.UninitialisedField(self, 'AsstClssSpcfcAttrbts', AssetClassAttributes1Choice, False)

	@AsstClssSpcfcAttrbts.deleter
	def AsstClssSpcfcAttrbts(self):
		del self._AsstClssSpcfcAttrbts
		self._AsstClssSpcfcAttrbts = base_types.UninitialisedField(self, 'AsstClssSpcfcAttrbts', AssetClassAttributes1Choice, False)

	@property
	def DlvryTp(self):
		return self._DlvryTp

	@DlvryTp.setter
	def DlvryTp(self, value):
		self._DlvryTp = value if value is not None else base_types.UninitialisedField(self, 'DlvryTp', PhysicalTransferType4Code, False)

	@DlvryTp.deleter
	def DlvryTp(self):
		del self._DlvryTp
		self._DlvryTp = base_types.UninitialisedField(self, 'DlvryTp', PhysicalTransferType4Code, False)

	@property
	def OptnExrcStyle(self):
		return self._OptnExrcStyle

	@OptnExrcStyle.setter
	def OptnExrcStyle(self, value):
		self._OptnExrcStyle = value if value is not None else base_types.UninitialisedField(self, 'OptnExrcStyle', OptionStyle7Code, False)

	@OptnExrcStyle.deleter
	def OptnExrcStyle(self):
		del self._OptnExrcStyle
		self._OptnExrcStyle = base_types.UninitialisedField(self, 'OptnExrcStyle', OptionStyle7Code, False)

	@property
	def OptnTp(self):
		return self._OptnTp

	@OptnTp.setter
	def OptnTp(self, value):
		self._OptnTp = value if value is not None else base_types.UninitialisedField(self, 'OptnTp', OptionType2Code, False)

	@OptnTp.deleter
	def OptnTp(self):
		del self._OptnTp
		self._OptnTp = base_types.UninitialisedField(self, 'OptnTp', OptionType2Code, False)

	@property
	def PricMltplr(self):
		return self._PricMltplr

	@PricMltplr.setter
	def PricMltplr(self, value):
		self._PricMltplr = value if value is not None else base_types.UninitialisedField(self, 'PricMltplr', NonNegativeDecimalNumber, False)

	@PricMltplr.deleter
	def PricMltplr(self):
		del self._PricMltplr
		self._PricMltplr = base_types.UninitialisedField(self, 'PricMltplr', NonNegativeDecimalNumber, False)

	@property
	def StrkPric(self):
		return self._StrkPric

	@StrkPric.setter
	def StrkPric(self, value):
		self._StrkPric = value if value is not None else base_types.UninitialisedField(self, 'StrkPric', SecuritiesTransactionPrice4Choice, False)

	@StrkPric.deleter
	def StrkPric(self):
		del self._StrkPric
		self._StrkPric = base_types.UninitialisedField(self, 'StrkPric', SecuritiesTransactionPrice4Choice, False)

	@property
	def UndrlygInstrm(self):
		return self._UndrlygInstrm

	@UndrlygInstrm.setter
	def UndrlygInstrm(self, value):
		self._UndrlygInstrm = value if value is not None else base_types.UninitialisedField(self, 'UndrlygInstrm', UnderlyingIdentification2Choice, False)

	@UndrlygInstrm.deleter
	def UndrlygInstrm(self):
		del self._UndrlygInstrm
		self._UndrlygInstrm = base_types.UninitialisedField(self, 'UndrlygInstrm', UnderlyingIdentification2Choice, False)

	@property
	def XpryDt(self):
		return self._XpryDt

	@XpryDt.setter
	def XpryDt(self, value):
		self._XpryDt = value if value is not None else base_types.UninitialisedField(self, 'XpryDt', ISODate, False)

	@XpryDt.deleter
	def XpryDt(self):
		del self._XpryDt
		self._XpryDt = base_types.UninitialisedField(self, 'XpryDt', ISODate, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AsstClssSpcfcAttrbts', type=AssetClassAttributes1Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DlvryTp', type=PhysicalTransferType4Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OptnExrcStyle', type=OptionStyle7Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OptnTp', type=OptionType2Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PricMltplr', type=NonNegativeDecimalNumber, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='StrkPric', type=SecuritiesTransactionPrice4Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='UndrlygInstrm', type=UnderlyingIdentification2Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='XpryDt', type=ISODate, min=0, max=1, mutex_group=None, array=False),
	))