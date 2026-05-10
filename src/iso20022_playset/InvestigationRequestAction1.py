from . import base_types
import InvestigationActionReason1
import InvestigationRequestAction1Choice

class InvestigationRequestAction1(base_types._BaseFieldType):

	__slots__ = ["_ActnRsn", "_Actn"]
	@property
	def ActnRsn(self):
		return self._ActnRsn

	@ActnRsn.setter
	def ActnRsn(self, value):
		self._ActnRsn = value if type(value) != auto else self.make_default("ActnRsn")

	@ActnRsn.deleter
	def ActnRsn(self):
		del self._ActnRsn
		self._ActnRsn = None

	@property
	def Actn(self):
		return self._Actn

	@Actn.setter
	def Actn(self, value):
		self._Actn = value if type(value) != auto else self.make_default("Actn")

	@Actn.deleter
	def Actn(self):
		del self._Actn
		self._Actn = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='ActnRsn', type=InvestigationActionReason1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Actn', type=InvestigationRequestAction1Choice, min=1, max=1, mutex_group=None, array=False),
	))

