# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._ErrorHandling5 import ErrorHandling5
from ._PartyAuditTrail2 import PartyAuditTrail2

class PartyAuditTrailOrError4Choice(base_types._BaseFieldType):

	__slots__ = ["_AudtTrl", "_BizErr"]
	@property
	def AudtTrl(self):
		return self._AudtTrl

	@AudtTrl.setter
	def AudtTrl(self, value):
		self._AudtTrl = value if type(value) != base_types.auto else self.make_default("AudtTrl")

	@AudtTrl.deleter
	def AudtTrl(self):
		del self._AudtTrl
		self._AudtTrl = None

	@property
	def BizErr(self):
		return self._BizErr

	@BizErr.setter
	def BizErr(self, value):
		self._BizErr = value if type(value) != base_types.auto else self.make_default("BizErr")

	@BizErr.deleter
	def BizErr(self):
		del self._BizErr
		self._BizErr = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='AudtTrl', type=PartyAuditTrail2, min=1, max=None, mutex_group=1, array=True),
		base_types.FieldEntry(name='BizErr', type=ErrorHandling5, min=1, max=None, mutex_group=1, array=True),
	))