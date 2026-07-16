# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import Algorithm11Code
from . import AlgorithmIdentification12
from . import Number

class Parameter8(base_types._BaseFieldType):

	__slots__ = ["_DgstAlgo", "_MskGnrtrAlgo", "_SaltLngth", "_TrlrFld"]
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
	def SaltLngth(self):
		return self._SaltLngth

	@SaltLngth.setter
	def SaltLngth(self, value):
		self._SaltLngth = value if value is not None else base_types.UninitialisedField(self, 'SaltLngth', Number, False)

	@SaltLngth.deleter
	def SaltLngth(self):
		del self._SaltLngth
		self._SaltLngth = base_types.UninitialisedField(self, 'SaltLngth', Number, False)

	@property
	def TrlrFld(self):
		return self._TrlrFld

	@TrlrFld.setter
	def TrlrFld(self, value):
		self._TrlrFld = value if value is not None else base_types.UninitialisedField(self, 'TrlrFld', Number, False)

	@TrlrFld.deleter
	def TrlrFld(self):
		del self._TrlrFld
		self._TrlrFld = base_types.UninitialisedField(self, 'TrlrFld', Number, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='DgstAlgo', type=Algorithm11Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MskGnrtrAlgo', type=AlgorithmIdentification12, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SaltLngth', type=Number, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TrlrFld', type=Number, min=0, max=1, mutex_group=None, array=False),
	))