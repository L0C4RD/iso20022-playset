# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import Max35Text
from . import RequestDetails4

class RequestDetails5(base_types._BaseFieldType):

	__slots__ = ["_ReqRef", "_RptKey", "_Tp"]
	@property
	def ReqRef(self):
		return self._ReqRef

	@ReqRef.setter
	def ReqRef(self, value):
		self._ReqRef = value if value is not None else base_types.UninitialisedField(self, 'ReqRef', Max35Text, False)

	@ReqRef.deleter
	def ReqRef(self):
		del self._ReqRef
		self._ReqRef = base_types.UninitialisedField(self, 'ReqRef', Max35Text, False)

	@property
	def RptKey(self):
		return self._RptKey

	@RptKey.setter
	def RptKey(self, value):
		self._RptKey = value if value is not None else base_types.UninitialisedField(self, 'RptKey', RequestDetails4, True)

	@RptKey.deleter
	def RptKey(self):
		del self._RptKey
		self._RptKey = base_types.UninitialisedField(self, 'RptKey', RequestDetails4, True)

	@property
	def Tp(self):
		return self._Tp

	@Tp.setter
	def Tp(self, value):
		self._Tp = value if value is not None else base_types.UninitialisedField(self, 'Tp', Max35Text, False)

	@Tp.deleter
	def Tp(self):
		del self._Tp
		self._Tp = base_types.UninitialisedField(self, 'Tp', Max35Text, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='ReqRef', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RptKey', type=RequestDetails4, min=1, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Tp', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
	))