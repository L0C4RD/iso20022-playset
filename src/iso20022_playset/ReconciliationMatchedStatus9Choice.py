from . import base_types
from .NoReasonCode import NoReasonCode
from .ReconciliationResult10 import ReconciliationResult10

class ReconciliationMatchedStatus9Choice(base_types._BaseFieldType):

	__slots__ = ["_NotMtchd", "_Mtchd"]
	@property
	def NotMtchd(self):
		return self._NotMtchd

	@NotMtchd.setter
	def NotMtchd(self, value):
		self._NotMtchd = value if type(value) != auto else self.make_default("NotMtchd")

	@NotMtchd.deleter
	def NotMtchd(self):
		del self._NotMtchd
		self._NotMtchd = None

	@property
	def Mtchd(self):
		return self._Mtchd

	@Mtchd.setter
	def Mtchd(self, value):
		self._Mtchd = value if type(value) != auto else self.make_default("Mtchd")

	@Mtchd.deleter
	def Mtchd(self):
		del self._Mtchd
		self._Mtchd = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='NotMtchd', type=ReconciliationResult10, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Mtchd', type=NoReasonCode, min=0, max=1, mutex_group=1, array=False),
	))

