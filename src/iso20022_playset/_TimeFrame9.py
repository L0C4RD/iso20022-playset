# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import BusinessDayConvention1Code
from . import Max350Text
from . import Number
from . import ReferToFundOrderDesk1Code

class TimeFrame9(base_types._BaseFieldType):

	__slots__ = ["_NonWorkgDayAdjstmnt", "_OthrTmFrameDesc", "_RefrToOrdrDsk", "_TMns"]
	@property
	def NonWorkgDayAdjstmnt(self):
		return self._NonWorkgDayAdjstmnt

	@NonWorkgDayAdjstmnt.setter
	def NonWorkgDayAdjstmnt(self, value):
		self._NonWorkgDayAdjstmnt = value if value is not None else base_types.UninitialisedField(self, 'NonWorkgDayAdjstmnt', BusinessDayConvention1Code, False)

	@NonWorkgDayAdjstmnt.deleter
	def NonWorkgDayAdjstmnt(self):
		del self._NonWorkgDayAdjstmnt
		self._NonWorkgDayAdjstmnt = base_types.UninitialisedField(self, 'NonWorkgDayAdjstmnt', BusinessDayConvention1Code, False)

	@property
	def OthrTmFrameDesc(self):
		return self._OthrTmFrameDesc

	@OthrTmFrameDesc.setter
	def OthrTmFrameDesc(self, value):
		self._OthrTmFrameDesc = value if value is not None else base_types.UninitialisedField(self, 'OthrTmFrameDesc', Max350Text, False)

	@OthrTmFrameDesc.deleter
	def OthrTmFrameDesc(self):
		del self._OthrTmFrameDesc
		self._OthrTmFrameDesc = base_types.UninitialisedField(self, 'OthrTmFrameDesc', Max350Text, False)

	@property
	def RefrToOrdrDsk(self):
		return self._RefrToOrdrDsk

	@RefrToOrdrDsk.setter
	def RefrToOrdrDsk(self, value):
		self._RefrToOrdrDsk = value if value is not None else base_types.UninitialisedField(self, 'RefrToOrdrDsk', ReferToFundOrderDesk1Code, False)

	@RefrToOrdrDsk.deleter
	def RefrToOrdrDsk(self):
		del self._RefrToOrdrDsk
		self._RefrToOrdrDsk = base_types.UninitialisedField(self, 'RefrToOrdrDsk', ReferToFundOrderDesk1Code, False)

	@property
	def TMns(self):
		return self._TMns

	@TMns.setter
	def TMns(self, value):
		self._TMns = value if value is not None else base_types.UninitialisedField(self, 'TMns', Number, False)

	@TMns.deleter
	def TMns(self):
		del self._TMns
		self._TMns = base_types.UninitialisedField(self, 'TMns', Number, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='NonWorkgDayAdjstmnt', type=BusinessDayConvention1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OthrTmFrameDesc', type=Max350Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RefrToOrdrDsk', type=ReferToFundOrderDesk1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TMns', type=Number, min=0, max=1, mutex_group=None, array=False),
	))