from . import base_types
import Algorithm5Code
import Max140Text

class AlgorithmAndDigest1(base_types._BaseFieldType):

	__slots__ = ["_DgstAlgo", "_Dgst"]
	@property
	def DgstAlgo(self):
		return self._DgstAlgo

	@DgstAlgo.setter
	def DgstAlgo(self, value):
		self._DgstAlgo = value if type(value) != auto else self.make_default("DgstAlgo")

	@DgstAlgo.deleter
	def DgstAlgo(self):
		del self._DgstAlgo
		self._DgstAlgo = None

	@property
	def Dgst(self):
		return self._Dgst

	@Dgst.setter
	def Dgst(self, value):
		self._Dgst = value if type(value) != auto else self.make_default("Dgst")

	@Dgst.deleter
	def Dgst(self):
		del self._Dgst
		self._Dgst = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='DgstAlgo', type=Algorithm5Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Dgst', type=Max140Text, min=1, max=1, mutex_group=None, array=False),
	))

