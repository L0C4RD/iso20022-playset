# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._BillingCancellationReport3 import BillingCancellationReport3
from ._BillingReport6 import BillingReport6
from ._ErrorHandling5 import ErrorHandling5

class BillingReportOrError6Choice(base_types._BaseFieldType):

	__slots__ = ["_BllgRpt", "_CxlRpt", "_OprlErr"]
	@property
	def BllgRpt(self):
		return self._BllgRpt

	@BllgRpt.setter
	def BllgRpt(self, value):
		self._BllgRpt = value if type(value) != base_types.auto else self.make_default("BllgRpt")

	@BllgRpt.deleter
	def BllgRpt(self):
		del self._BllgRpt
		self._BllgRpt = None

	@property
	def CxlRpt(self):
		return self._CxlRpt

	@CxlRpt.setter
	def CxlRpt(self, value):
		self._CxlRpt = value if type(value) != base_types.auto else self.make_default("CxlRpt")

	@CxlRpt.deleter
	def CxlRpt(self):
		del self._CxlRpt
		self._CxlRpt = None

	@property
	def OprlErr(self):
		return self._OprlErr

	@OprlErr.setter
	def OprlErr(self, value):
		self._OprlErr = value if type(value) != base_types.auto else self.make_default("OprlErr")

	@OprlErr.deleter
	def OprlErr(self):
		del self._OprlErr
		self._OprlErr = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='BllgRpt', type=BillingReport6, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='CxlRpt', type=BillingCancellationReport3, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='OprlErr', type=ErrorHandling5, min=1, max=None, mutex_group=1, array=True),
	))