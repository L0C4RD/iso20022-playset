# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import Algorithm11Code
from . import AlgorithmIdentification12
from . import EncryptionFormat1Code

class Parameter4(base_types._BaseFieldType):

	__slots__ = ["_DgstAlgo", "_MskGnrtrAlgo", "_NcrptnFrmt"]
	@property
	def DgstAlgo(self):
		return self._DgstAlgo

	@DgstAlgo.setter
	def DgstAlgo(self, value):
		self._DgstAlgo = value if value is not None else base_types.UninitialisedField(self, 'DgstAlgo', Algorithm11Code, False)

	@DgstAlgo.deleter
	def DgstAlgo(self):
		del self._DgstAlgo
		self._DgstAlgo = base_types.UninitialisedField(self, 'DgstAlgo', Algorithm11Code, False)

	@property
	def MskGnrtrAlgo(self):
		return self._MskGnrtrAlgo

	@MskGnrtrAlgo.setter
	def MskGnrtrAlgo(self, value):
		self._MskGnrtrAlgo = value if value is not None else base_types.UninitialisedField(self, 'MskGnrtrAlgo', AlgorithmIdentification12, False)

	@MskGnrtrAlgo.deleter
	def MskGnrtrAlgo(self):
		del self._MskGnrtrAlgo
		self._MskGnrtrAlgo = base_types.UninitialisedField(self, 'MskGnrtrAlgo', AlgorithmIdentification12, False)

	@property
	def NcrptnFrmt(self):
		return self._NcrptnFrmt

	@NcrptnFrmt.setter
	def NcrptnFrmt(self, value):
		self._NcrptnFrmt = value if value is not None else base_types.UninitialisedField(self, 'NcrptnFrmt', EncryptionFormat1Code, False)

	@NcrptnFrmt.deleter
	def NcrptnFrmt(self):
		del self._NcrptnFrmt
		self._NcrptnFrmt = base_types.UninitialisedField(self, 'NcrptnFrmt', EncryptionFormat1Code, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='DgstAlgo', type=Algorithm11Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MskGnrtrAlgo', type=AlgorithmIdentification12, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NcrptnFrmt', type=EncryptionFormat1Code, min=0, max=1, mutex_group=None, array=False),
	))