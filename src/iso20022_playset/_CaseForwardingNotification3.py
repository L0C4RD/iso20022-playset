# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import CaseForwardingNotification3Code

class CaseForwardingNotification3(base_types._BaseFieldType):

	__slots__ = ["_Justfn"]
	@property
	def Justfn(self):
		return self._Justfn

	@Justfn.setter
	def Justfn(self, value):
		self._Justfn = value if value is not None else base_types.UninitialisedField(self, 'Justfn', CaseForwardingNotification3Code, False)

	@Justfn.deleter
	def Justfn(self):
		del self._Justfn
		self._Justfn = base_types.UninitialisedField(self, 'Justfn', CaseForwardingNotification3Code, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Justfn', type=CaseForwardingNotification3Code, min=1, max=1, mutex_group=None, array=False),
	))