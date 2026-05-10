from . import base_types
from ._CaseForwardingNotification3Code import CaseForwardingNotification3Code

class CaseForwardingNotification3(base_types._BaseFieldType):

	__slots__ = ["_Justfn"]
	@property
	def Justfn(self):
		return self._Justfn

	@Justfn.setter
	def Justfn(self, value):
		self._Justfn = value if type(value) != base_types.auto else self.make_default("Justfn")

	@Justfn.deleter
	def Justfn(self):
		del self._Justfn
		self._Justfn = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Justfn', type=CaseForwardingNotification3Code, min=1, max=1, mutex_group=None, array=False),
	))

