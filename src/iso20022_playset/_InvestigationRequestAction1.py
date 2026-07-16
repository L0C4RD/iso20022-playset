# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import InvestigationActionReason1
from . import InvestigationRequestAction1Choice

class InvestigationRequestAction1(base_types._BaseFieldType):

	__slots__ = ["_Actn", "_ActnRsn"]
	@property
	def Actn(self):
		return self._Actn

	@Actn.setter
	def Actn(self, value):
		self._Actn = value if value is not None else base_types.UninitialisedField(self, 'Actn', InvestigationRequestAction1Choice, False)

	@Actn.deleter
	def Actn(self):
		del self._Actn
		self._Actn = base_types.UninitialisedField(self, 'Actn', InvestigationRequestAction1Choice, False)

	@property
	def ActnRsn(self):
		return self._ActnRsn

	@ActnRsn.setter
	def ActnRsn(self, value):
		self._ActnRsn = value if value is not None else base_types.UninitialisedField(self, 'ActnRsn', InvestigationActionReason1, False)

	@ActnRsn.deleter
	def ActnRsn(self):
		del self._ActnRsn
		self._ActnRsn = base_types.UninitialisedField(self, 'ActnRsn', InvestigationActionReason1, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Actn', type=InvestigationRequestAction1Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ActnRsn', type=InvestigationActionReason1, min=0, max=1, mutex_group=None, array=False),
	))