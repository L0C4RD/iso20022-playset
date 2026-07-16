# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ReportLine5
from . import ReportLine6

class BreakDown1Choice(base_types._BaseFieldType):

	__slots__ = ["_ByComrclInvc", "_ByPurchsOrdr"]
	@property
	def ByComrclInvc(self):
		return self._ByComrclInvc

	@ByComrclInvc.setter
	def ByComrclInvc(self, value):
		self._ByComrclInvc = value if value is not None else base_types.UninitialisedField(self, 'ByComrclInvc', ReportLine6, False)

	@ByComrclInvc.deleter
	def ByComrclInvc(self):
		del self._ByComrclInvc
		self._ByComrclInvc = base_types.UninitialisedField(self, 'ByComrclInvc', ReportLine6, False)

	@property
	def ByPurchsOrdr(self):
		return self._ByPurchsOrdr

	@ByPurchsOrdr.setter
	def ByPurchsOrdr(self, value):
		self._ByPurchsOrdr = value if value is not None else base_types.UninitialisedField(self, 'ByPurchsOrdr', ReportLine5, False)

	@ByPurchsOrdr.deleter
	def ByPurchsOrdr(self):
		del self._ByPurchsOrdr
		self._ByPurchsOrdr = base_types.UninitialisedField(self, 'ByPurchsOrdr', ReportLine5, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='ByComrclInvc', type=ReportLine6, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='ByPurchsOrdr', type=ReportLine5, min=0, max=1, mutex_group=1, array=False),
	))