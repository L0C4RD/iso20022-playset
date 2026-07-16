# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ErrorHandling5
from . import PartyAuditTrail2

class PartyAuditTrailOrError4Choice(base_types._BaseFieldType):

	__slots__ = ["_AudtTrl", "_BizErr"]
	@property
	def AudtTrl(self):
		return self._AudtTrl

	@AudtTrl.setter
	def AudtTrl(self, value):
		self._AudtTrl = value if value is not None else base_types.UninitialisedField(self, 'AudtTrl', PartyAuditTrail2, True)

	@AudtTrl.deleter
	def AudtTrl(self):
		del self._AudtTrl
		self._AudtTrl = base_types.UninitialisedField(self, 'AudtTrl', PartyAuditTrail2, True)

	@property
	def BizErr(self):
		return self._BizErr

	@BizErr.setter
	def BizErr(self, value):
		self._BizErr = value if value is not None else base_types.UninitialisedField(self, 'BizErr', ErrorHandling5, True)

	@BizErr.deleter
	def BizErr(self):
		del self._BizErr
		self._BizErr = base_types.UninitialisedField(self, 'BizErr', ErrorHandling5, True)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AudtTrl', type=PartyAuditTrail2, min=1, max=None, mutex_group=1, array=True),
		base_types.FieldEntry(name='BizErr', type=ErrorHandling5, min=1, max=None, mutex_group=1, array=True),
	))