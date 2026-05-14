# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._AttestationValue1Code import AttestationValue1Code
from ._Exemption2Code import Exemption2Code
from ._Max4Text import Max4Text

class Exemption2(base_types._BaseFieldType):

	__slots__ = ["_RsnNotHnrd", "_Tp", "_Val"]
	@property
	def RsnNotHnrd(self):
		return self._RsnNotHnrd

	@RsnNotHnrd.setter
	def RsnNotHnrd(self, value):
		self._RsnNotHnrd = value if type(value) != base_types.auto else self.make_default("RsnNotHnrd")

	@RsnNotHnrd.deleter
	def RsnNotHnrd(self):
		del self._RsnNotHnrd
		self._RsnNotHnrd = None

	@property
	def Tp(self):
		return self._Tp

	@Tp.setter
	def Tp(self, value):
		self._Tp = value if type(value) != base_types.auto else self.make_default("Tp")

	@Tp.deleter
	def Tp(self):
		del self._Tp
		self._Tp = None

	@property
	def Val(self):
		return self._Val

	@Val.setter
	def Val(self, value):
		self._Val = value if type(value) != base_types.auto else self.make_default("Val")

	@Val.deleter
	def Val(self):
		del self._Val
		self._Val = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='RsnNotHnrd', type=Max4Text, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Tp', type=Exemption2Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Val', type=AttestationValue1Code, min=1, max=1, mutex_group=None, array=False),
	))