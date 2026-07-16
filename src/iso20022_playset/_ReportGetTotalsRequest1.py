# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import TotalDetails1Code
from . import TotalFilter1

class ReportGetTotalsRequest1(base_types._BaseFieldType):

	__slots__ = ["_TtlDtls", "_TtlFltr"]
	@property
	def TtlDtls(self):
		return self._TtlDtls

	@TtlDtls.setter
	def TtlDtls(self, value):
		self._TtlDtls = value if value is not None else base_types.UninitialisedField(self, 'TtlDtls', TotalDetails1Code, False)

	@TtlDtls.deleter
	def TtlDtls(self):
		del self._TtlDtls
		self._TtlDtls = base_types.UninitialisedField(self, 'TtlDtls', TotalDetails1Code, False)

	@property
	def TtlFltr(self):
		return self._TtlFltr

	@TtlFltr.setter
	def TtlFltr(self, value):
		self._TtlFltr = value if value is not None else base_types.UninitialisedField(self, 'TtlFltr', TotalFilter1, False)

	@TtlFltr.deleter
	def TtlFltr(self):
		del self._TtlFltr
		self._TtlFltr = base_types.UninitialisedField(self, 'TtlFltr', TotalFilter1, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='TtlDtls', type=TotalDetails1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TtlFltr', type=TotalFilter1, min=0, max=1, mutex_group=None, array=False),
	))