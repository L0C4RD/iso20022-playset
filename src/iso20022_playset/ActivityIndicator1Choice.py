import base_types
import ISICIdentifier
import GenericIdentification36

class ActivityIndicator1Choice(base_types._BaseFieldType):

	__slots__ = ["_PrtryInd", "_ISICIdr"]
	@property
	def PrtryInd(self):
		return self._PrtryInd

	@PrtryInd.setter
	def PrtryInd(self, value):
		self._PrtryInd = value if type(value) != auto else self.make_default("PrtryInd")

	@PrtryInd.deleter
	def PrtryInd(self):
		del self._PrtryInd
		self._PrtryInd = None

	@property
	def ISICIdr(self):
		return self._ISICIdr

	@ISICIdr.setter
	def ISICIdr(self, value):
		self._ISICIdr = value if type(value) != auto else self.make_default("ISICIdr")

	@ISICIdr.deleter
	def ISICIdr(self):
		del self._ISICIdr
		self._ISICIdr = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='PrtryInd', type=GenericIdentification36, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='ISICIdr', type=ISICIdentifier, min=0, max=1, mutex_group=1, array=False),
	))

