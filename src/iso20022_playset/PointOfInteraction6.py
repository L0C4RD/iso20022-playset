import base_types
import Max35Text

class PointOfInteraction6(base_types._BaseFieldType):

	__slots__ = ["_Mdl", "_SrlNb", "_ManfctrIdr"]
	@property
	def Mdl(self):
		return self._Mdl

	@Mdl.setter
	def Mdl(self, value):
		self._Mdl = value if type(value) != auto else self.make_default("Mdl")

	@Mdl.deleter
	def Mdl(self):
		del self._Mdl
		self._Mdl = None

	@property
	def SrlNb(self):
		return self._SrlNb

	@SrlNb.setter
	def SrlNb(self, value):
		self._SrlNb = value if type(value) != auto else self.make_default("SrlNb")

	@SrlNb.deleter
	def SrlNb(self):
		del self._SrlNb
		self._SrlNb = None

	@property
	def ManfctrIdr(self):
		return self._ManfctrIdr

	@ManfctrIdr.setter
	def ManfctrIdr(self, value):
		self._ManfctrIdr = value if type(value) != auto else self.make_default("ManfctrIdr")

	@ManfctrIdr.deleter
	def ManfctrIdr(self):
		del self._ManfctrIdr
		self._ManfctrIdr = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Mdl', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SrlNb', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ManfctrIdr', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
	))

