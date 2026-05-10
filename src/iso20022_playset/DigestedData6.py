import base_types
import Max140Binary
import EncapsulatedContent3
import AlgorithmIdentification36
import Number

class DigestedData6(base_types._BaseFieldType):

	__slots__ = ["_NcpsltdCntt", "_DgstAlgo", "_Vrsn", "_Dgst"]
	@property
	def NcpsltdCntt(self):
		return self._NcpsltdCntt

	@NcpsltdCntt.setter
	def NcpsltdCntt(self, value):
		self._NcpsltdCntt = value if type(value) != auto else self.make_default("NcpsltdCntt")

	@NcpsltdCntt.deleter
	def NcpsltdCntt(self):
		del self._NcpsltdCntt
		self._NcpsltdCntt = None

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
	def Vrsn(self):
		return self._Vrsn

	@Vrsn.setter
	def Vrsn(self, value):
		self._Vrsn = value if type(value) != auto else self.make_default("Vrsn")

	@Vrsn.deleter
	def Vrsn(self):
		del self._Vrsn
		self._Vrsn = None

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
		base_types.FieldEntry(name='NcpsltdCntt', type=EncapsulatedContent3, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DgstAlgo', type=AlgorithmIdentification36, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Vrsn', type=Number, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Dgst', type=Max140Binary, min=1, max=1, mutex_group=None, array=False),
	))

