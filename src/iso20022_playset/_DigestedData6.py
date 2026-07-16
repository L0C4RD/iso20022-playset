# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import AlgorithmIdentification36
from . import EncapsulatedContent3
from . import Max140Binary
from . import Number

class DigestedData6(base_types._BaseFieldType):

	__slots__ = ["_Dgst", "_DgstAlgo", "_NcpsltdCntt", "_Vrsn"]
	@property
	def Dgst(self):
		return self._Dgst

	@Dgst.setter
	def Dgst(self, value):
		self._Dgst = value if value is not None else base_types.UninitialisedField(self, 'Dgst', Max140Binary, False)

	@Dgst.deleter
	def Dgst(self):
		del self._Dgst
		self._Dgst = base_types.UninitialisedField(self, 'Dgst', Max140Binary, False)

	@property
	def DgstAlgo(self):
		return self._DgstAlgo

	@DgstAlgo.setter
	def DgstAlgo(self, value):
		self._DgstAlgo = value if value is not None else base_types.UninitialisedField(self, 'DgstAlgo', AlgorithmIdentification36, False)

	@DgstAlgo.deleter
	def DgstAlgo(self):
		del self._DgstAlgo
		self._DgstAlgo = base_types.UninitialisedField(self, 'DgstAlgo', AlgorithmIdentification36, False)

	@property
	def NcpsltdCntt(self):
		return self._NcpsltdCntt

	@NcpsltdCntt.setter
	def NcpsltdCntt(self, value):
		self._NcpsltdCntt = value if value is not None else base_types.UninitialisedField(self, 'NcpsltdCntt', EncapsulatedContent3, False)

	@NcpsltdCntt.deleter
	def NcpsltdCntt(self):
		del self._NcpsltdCntt
		self._NcpsltdCntt = base_types.UninitialisedField(self, 'NcpsltdCntt', EncapsulatedContent3, False)

	@property
	def Vrsn(self):
		return self._Vrsn

	@Vrsn.setter
	def Vrsn(self, value):
		self._Vrsn = value if value is not None else base_types.UninitialisedField(self, 'Vrsn', Number, False)

	@Vrsn.deleter
	def Vrsn(self):
		del self._Vrsn
		self._Vrsn = base_types.UninitialisedField(self, 'Vrsn', Number, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Dgst', type=Max140Binary, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DgstAlgo', type=AlgorithmIdentification36, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NcpsltdCntt', type=EncapsulatedContent3, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Vrsn', type=Number, min=0, max=1, mutex_group=None, array=False),
	))