# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import InvestigationRejection1Code

class InvestigationRejectionJustification1(base_types._BaseFieldType):

	__slots__ = ["_RjctnRsn"]
	@property
	def RjctnRsn(self):
		return self._RjctnRsn

	@RjctnRsn.setter
	def RjctnRsn(self, value):
		self._RjctnRsn = value if value is not None else base_types.UninitialisedField(self, 'RjctnRsn', InvestigationRejection1Code, False)

	@RjctnRsn.deleter
	def RjctnRsn(self):
		del self._RjctnRsn
		self._RjctnRsn = base_types.UninitialisedField(self, 'RjctnRsn', InvestigationRejection1Code, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='RjctnRsn', type=InvestigationRejection1Code, min=1, max=1, mutex_group=None, array=False),
	))