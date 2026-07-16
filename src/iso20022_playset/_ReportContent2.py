# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import Max10NumericText
from . import ReportContent2Choice

class ReportContent2(base_types._BaseFieldType):

	__slots__ = ["_FrmtdCntt", "_RptLineSeq"]
	@property
	def FrmtdCntt(self):
		return self._FrmtdCntt

	@FrmtdCntt.setter
	def FrmtdCntt(self, value):
		self._FrmtdCntt = value if value is not None else base_types.UninitialisedField(self, 'FrmtdCntt', ReportContent2Choice, False)

	@FrmtdCntt.deleter
	def FrmtdCntt(self):
		del self._FrmtdCntt
		self._FrmtdCntt = base_types.UninitialisedField(self, 'FrmtdCntt', ReportContent2Choice, False)

	@property
	def RptLineSeq(self):
		return self._RptLineSeq

	@RptLineSeq.setter
	def RptLineSeq(self, value):
		self._RptLineSeq = value if value is not None else base_types.UninitialisedField(self, 'RptLineSeq', Max10NumericText, False)

	@RptLineSeq.deleter
	def RptLineSeq(self):
		del self._RptLineSeq
		self._RptLineSeq = base_types.UninitialisedField(self, 'RptLineSeq', Max10NumericText, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='FrmtdCntt', type=ReportContent2Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RptLineSeq', type=Max10NumericText, min=0, max=1, mutex_group=None, array=False),
	))