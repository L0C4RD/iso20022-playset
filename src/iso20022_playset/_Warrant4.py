# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import BaseOneRate
from . import Organisation38
from . import Price8
from . import WarrantStyle3Choice

class Warrant4(base_types._BaseFieldType):

	__slots__ = ["_Mltplr", "_SbcptPric", "_Tp", "_WarrtAgt"]
	@property
	def Mltplr(self):
		return self._Mltplr

	@Mltplr.setter
	def Mltplr(self, value):
		self._Mltplr = value if value is not None else base_types.UninitialisedField(self, 'Mltplr', BaseOneRate, False)

	@Mltplr.deleter
	def Mltplr(self):
		del self._Mltplr
		self._Mltplr = base_types.UninitialisedField(self, 'Mltplr', BaseOneRate, False)

	@property
	def SbcptPric(self):
		return self._SbcptPric

	@SbcptPric.setter
	def SbcptPric(self, value):
		self._SbcptPric = value if value is not None else base_types.UninitialisedField(self, 'SbcptPric', Price8, False)

	@SbcptPric.deleter
	def SbcptPric(self):
		del self._SbcptPric
		self._SbcptPric = base_types.UninitialisedField(self, 'SbcptPric', Price8, False)

	@property
	def Tp(self):
		return self._Tp

	@Tp.setter
	def Tp(self, value):
		self._Tp = value if value is not None else base_types.UninitialisedField(self, 'Tp', WarrantStyle3Choice, False)

	@Tp.deleter
	def Tp(self):
		del self._Tp
		self._Tp = base_types.UninitialisedField(self, 'Tp', WarrantStyle3Choice, False)

	@property
	def WarrtAgt(self):
		return self._WarrtAgt

	@WarrtAgt.setter
	def WarrtAgt(self, value):
		self._WarrtAgt = value if value is not None else base_types.UninitialisedField(self, 'WarrtAgt', Organisation38, True)

	@WarrtAgt.deleter
	def WarrtAgt(self):
		del self._WarrtAgt
		self._WarrtAgt = base_types.UninitialisedField(self, 'WarrtAgt', Organisation38, True)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Mltplr', type=BaseOneRate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SbcptPric', type=Price8, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Tp', type=WarrantStyle3Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='WarrtAgt', type=Organisation38, min=0, max=None, mutex_group=None, array=True),
	))