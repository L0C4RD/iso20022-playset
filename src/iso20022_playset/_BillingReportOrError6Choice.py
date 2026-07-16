# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import BillingCancellationReport3
from . import BillingReport6
from . import ErrorHandling5

class BillingReportOrError6Choice(base_types._BaseFieldType):

	__slots__ = ["_BllgRpt", "_CxlRpt", "_OprlErr"]
	@property
	def BllgRpt(self):
		return self._BllgRpt

	@BllgRpt.setter
	def BllgRpt(self, value):
		self._BllgRpt = value if value is not None else base_types.UninitialisedField(self, 'BllgRpt', BillingReport6, False)

	@BllgRpt.deleter
	def BllgRpt(self):
		del self._BllgRpt
		self._BllgRpt = base_types.UninitialisedField(self, 'BllgRpt', BillingReport6, False)

	@property
	def CxlRpt(self):
		return self._CxlRpt

	@CxlRpt.setter
	def CxlRpt(self, value):
		self._CxlRpt = value if value is not None else base_types.UninitialisedField(self, 'CxlRpt', BillingCancellationReport3, False)

	@CxlRpt.deleter
	def CxlRpt(self):
		del self._CxlRpt
		self._CxlRpt = base_types.UninitialisedField(self, 'CxlRpt', BillingCancellationReport3, False)

	@property
	def OprlErr(self):
		return self._OprlErr

	@OprlErr.setter
	def OprlErr(self, value):
		self._OprlErr = value if value is not None else base_types.UninitialisedField(self, 'OprlErr', ErrorHandling5, True)

	@OprlErr.deleter
	def OprlErr(self):
		del self._OprlErr
		self._OprlErr = base_types.UninitialisedField(self, 'OprlErr', ErrorHandling5, True)

	_field_defs = frozenset((
		base_types.FieldEntry(name='BllgRpt', type=BillingReport6, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='CxlRpt', type=BillingCancellationReport3, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='OprlErr', type=ErrorHandling5, min=1, max=None, mutex_group=1, array=True),
	))