# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._ActiveCurrencyCode import ActiveCurrencyCode
from ._GenericIdentification168 import GenericIdentification168
from ._Max2000Text import Max2000Text
from ._Max35Text import Max35Text

class LiquidityStressScenarioDefinition1(base_types._BaseFieldType):

	__slots__ = ["_Desc", "_Id", "_StrssCcy", "_Tp"]
	@property
	def Desc(self):
		return self._Desc

	@Desc.setter
	def Desc(self, value):
		self._Desc = value if type(value) != base_types.auto else self.make_default("Desc")

	@Desc.deleter
	def Desc(self):
		del self._Desc
		self._Desc = None

	@property
	def Id(self):
		return self._Id

	@Id.setter
	def Id(self, value):
		self._Id = value if type(value) != base_types.auto else self.make_default("Id")

	@Id.deleter
	def Id(self):
		del self._Id
		self._Id = None

	@property
	def StrssCcy(self):
		return self._StrssCcy

	@StrssCcy.setter
	def StrssCcy(self, value):
		self._StrssCcy = value if type(value) != base_types.auto else self.make_default("StrssCcy")

	@StrssCcy.deleter
	def StrssCcy(self):
		del self._StrssCcy
		self._StrssCcy = None

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

	_field_defs = frozenset((
		base_types.FieldEntry(name='Desc', type=Max2000Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Id', type=GenericIdentification168, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='StrssCcy', type=ActiveCurrencyCode, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Tp', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
	))