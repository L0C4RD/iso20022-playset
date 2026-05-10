import base_types
import Max35Text
import Fee7

class Fees2(base_types._BaseFieldType):

	__slots__ = ["_IndvFee", "_ComrclAgrmtRef"]
	@property
	def IndvFee(self):
		return self._IndvFee

	@IndvFee.setter
	def IndvFee(self, value):
		self._IndvFee = value if type(value) != auto else self.make_default("IndvFee")

	@IndvFee.deleter
	def IndvFee(self):
		del self._IndvFee
		self._IndvFee = None

	@property
	def ComrclAgrmtRef(self):
		return self._ComrclAgrmtRef

	@ComrclAgrmtRef.setter
	def ComrclAgrmtRef(self, value):
		self._ComrclAgrmtRef = value if type(value) != auto else self.make_default("ComrclAgrmtRef")

	@ComrclAgrmtRef.deleter
	def ComrclAgrmtRef(self):
		del self._ComrclAgrmtRef
		self._ComrclAgrmtRef = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='IndvFee', type=Fee7, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='ComrclAgrmtRef', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
	))

