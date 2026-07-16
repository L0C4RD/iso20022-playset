# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import Algorithm5Code
from . import Max140Text

class AlgorithmAndDigest1(base_types._BaseFieldType):

	__slots__ = ["_Dgst", "_DgstAlgo"]
	@property
	def Dgst(self):
		return self._Dgst

	@Dgst.setter
	def Dgst(self, value):
		self._Dgst = value if value is not None else base_types.UninitialisedField(self, 'Dgst', Max140Text, False)

	@Dgst.deleter
	def Dgst(self):
		del self._Dgst
		self._Dgst = base_types.UninitialisedField(self, 'Dgst', Max140Text, False)

	@property
	def DgstAlgo(self):
		return self._DgstAlgo

	@DgstAlgo.setter
	def DgstAlgo(self, value):
		self._DgstAlgo = value if value is not None else base_types.UninitialisedField(self, 'DgstAlgo', Algorithm5Code, False)

	@DgstAlgo.deleter
	def DgstAlgo(self):
		del self._DgstAlgo
		self._DgstAlgo = base_types.UninitialisedField(self, 'DgstAlgo', Algorithm5Code, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Dgst', type=Max140Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DgstAlgo', type=Algorithm5Code, min=1, max=1, mutex_group=None, array=False),
	))