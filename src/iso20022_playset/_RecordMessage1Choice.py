# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._Max2MBBinary import Max2MBBinary

class RecordMessage1Choice(base_types._BaseFieldType):

	__slots__ = ["_AdddmInitn", "_AdddmRspn", "_Amdmnt", "_AuthstnInitn", "_AuthstnRspn", "_CardMgmtInitn", "_CardMgmtRspn", "_ChrgBckInitn", "_ChrgBckRspn", "_Err", "_FeeColltnInitn", "_FeeColltnRspn", "_FileActnInitn", "_FileActnRspn", "_FinInitn", "_FinRspn", "_FrdDspstnInitn", "_FrdDspstnRspn", "_FrdRptgInitn", "_FrdRptgRspn", "_KeyXchgInitn", "_KeyXchgRspn", "_NqryInitn", "_NqryRspn", "_NtwkMgmtInitn", "_NtwkMgmtRspn", "_RcncltnInitn", "_RcncltnRspn", "_RtrvlFlfmtInitn", "_RtrvlFlfmtRspn", "_RtrvlInitn", "_RtrvlRspn", "_RvslInitn", "_RvslRspn", "_SttlmRptgInitn", "_SttlmRptgRspn", "_VrfctnInitn", "_VrfctnRspn"]
	@property
	def AdddmInitn(self):
		return self._AdddmInitn

	@AdddmInitn.setter
	def AdddmInitn(self, value):
		self._AdddmInitn = value if type(value) != base_types.auto else self.make_default("AdddmInitn")

	@AdddmInitn.deleter
	def AdddmInitn(self):
		del self._AdddmInitn
		self._AdddmInitn = None

	@property
	def AdddmRspn(self):
		return self._AdddmRspn

	@AdddmRspn.setter
	def AdddmRspn(self, value):
		self._AdddmRspn = value if type(value) != base_types.auto else self.make_default("AdddmRspn")

	@AdddmRspn.deleter
	def AdddmRspn(self):
		del self._AdddmRspn
		self._AdddmRspn = None

	@property
	def Amdmnt(self):
		return self._Amdmnt

	@Amdmnt.setter
	def Amdmnt(self, value):
		self._Amdmnt = value if type(value) != base_types.auto else self.make_default("Amdmnt")

	@Amdmnt.deleter
	def Amdmnt(self):
		del self._Amdmnt
		self._Amdmnt = None

	@property
	def AuthstnInitn(self):
		return self._AuthstnInitn

	@AuthstnInitn.setter
	def AuthstnInitn(self, value):
		self._AuthstnInitn = value if type(value) != base_types.auto else self.make_default("AuthstnInitn")

	@AuthstnInitn.deleter
	def AuthstnInitn(self):
		del self._AuthstnInitn
		self._AuthstnInitn = None

	@property
	def AuthstnRspn(self):
		return self._AuthstnRspn

	@AuthstnRspn.setter
	def AuthstnRspn(self, value):
		self._AuthstnRspn = value if type(value) != base_types.auto else self.make_default("AuthstnRspn")

	@AuthstnRspn.deleter
	def AuthstnRspn(self):
		del self._AuthstnRspn
		self._AuthstnRspn = None

	@property
	def CardMgmtInitn(self):
		return self._CardMgmtInitn

	@CardMgmtInitn.setter
	def CardMgmtInitn(self, value):
		self._CardMgmtInitn = value if type(value) != base_types.auto else self.make_default("CardMgmtInitn")

	@CardMgmtInitn.deleter
	def CardMgmtInitn(self):
		del self._CardMgmtInitn
		self._CardMgmtInitn = None

	@property
	def CardMgmtRspn(self):
		return self._CardMgmtRspn

	@CardMgmtRspn.setter
	def CardMgmtRspn(self, value):
		self._CardMgmtRspn = value if type(value) != base_types.auto else self.make_default("CardMgmtRspn")

	@CardMgmtRspn.deleter
	def CardMgmtRspn(self):
		del self._CardMgmtRspn
		self._CardMgmtRspn = None

	@property
	def ChrgBckInitn(self):
		return self._ChrgBckInitn

	@ChrgBckInitn.setter
	def ChrgBckInitn(self, value):
		self._ChrgBckInitn = value if type(value) != base_types.auto else self.make_default("ChrgBckInitn")

	@ChrgBckInitn.deleter
	def ChrgBckInitn(self):
		del self._ChrgBckInitn
		self._ChrgBckInitn = None

	@property
	def ChrgBckRspn(self):
		return self._ChrgBckRspn

	@ChrgBckRspn.setter
	def ChrgBckRspn(self, value):
		self._ChrgBckRspn = value if type(value) != base_types.auto else self.make_default("ChrgBckRspn")

	@ChrgBckRspn.deleter
	def ChrgBckRspn(self):
		del self._ChrgBckRspn
		self._ChrgBckRspn = None

	@property
	def Err(self):
		return self._Err

	@Err.setter
	def Err(self, value):
		self._Err = value if type(value) != base_types.auto else self.make_default("Err")

	@Err.deleter
	def Err(self):
		del self._Err
		self._Err = None

	@property
	def FeeColltnInitn(self):
		return self._FeeColltnInitn

	@FeeColltnInitn.setter
	def FeeColltnInitn(self, value):
		self._FeeColltnInitn = value if type(value) != base_types.auto else self.make_default("FeeColltnInitn")

	@FeeColltnInitn.deleter
	def FeeColltnInitn(self):
		del self._FeeColltnInitn
		self._FeeColltnInitn = None

	@property
	def FeeColltnRspn(self):
		return self._FeeColltnRspn

	@FeeColltnRspn.setter
	def FeeColltnRspn(self, value):
		self._FeeColltnRspn = value if type(value) != base_types.auto else self.make_default("FeeColltnRspn")

	@FeeColltnRspn.deleter
	def FeeColltnRspn(self):
		del self._FeeColltnRspn
		self._FeeColltnRspn = None

	@property
	def FileActnInitn(self):
		return self._FileActnInitn

	@FileActnInitn.setter
	def FileActnInitn(self, value):
		self._FileActnInitn = value if type(value) != base_types.auto else self.make_default("FileActnInitn")

	@FileActnInitn.deleter
	def FileActnInitn(self):
		del self._FileActnInitn
		self._FileActnInitn = None

	@property
	def FileActnRspn(self):
		return self._FileActnRspn

	@FileActnRspn.setter
	def FileActnRspn(self, value):
		self._FileActnRspn = value if type(value) != base_types.auto else self.make_default("FileActnRspn")

	@FileActnRspn.deleter
	def FileActnRspn(self):
		del self._FileActnRspn
		self._FileActnRspn = None

	@property
	def FinInitn(self):
		return self._FinInitn

	@FinInitn.setter
	def FinInitn(self, value):
		self._FinInitn = value if type(value) != base_types.auto else self.make_default("FinInitn")

	@FinInitn.deleter
	def FinInitn(self):
		del self._FinInitn
		self._FinInitn = None

	@property
	def FinRspn(self):
		return self._FinRspn

	@FinRspn.setter
	def FinRspn(self, value):
		self._FinRspn = value if type(value) != base_types.auto else self.make_default("FinRspn")

	@FinRspn.deleter
	def FinRspn(self):
		del self._FinRspn
		self._FinRspn = None

	@property
	def FrdDspstnInitn(self):
		return self._FrdDspstnInitn

	@FrdDspstnInitn.setter
	def FrdDspstnInitn(self, value):
		self._FrdDspstnInitn = value if type(value) != base_types.auto else self.make_default("FrdDspstnInitn")

	@FrdDspstnInitn.deleter
	def FrdDspstnInitn(self):
		del self._FrdDspstnInitn
		self._FrdDspstnInitn = None

	@property
	def FrdDspstnRspn(self):
		return self._FrdDspstnRspn

	@FrdDspstnRspn.setter
	def FrdDspstnRspn(self, value):
		self._FrdDspstnRspn = value if type(value) != base_types.auto else self.make_default("FrdDspstnRspn")

	@FrdDspstnRspn.deleter
	def FrdDspstnRspn(self):
		del self._FrdDspstnRspn
		self._FrdDspstnRspn = None

	@property
	def FrdRptgInitn(self):
		return self._FrdRptgInitn

	@FrdRptgInitn.setter
	def FrdRptgInitn(self, value):
		self._FrdRptgInitn = value if type(value) != base_types.auto else self.make_default("FrdRptgInitn")

	@FrdRptgInitn.deleter
	def FrdRptgInitn(self):
		del self._FrdRptgInitn
		self._FrdRptgInitn = None

	@property
	def FrdRptgRspn(self):
		return self._FrdRptgRspn

	@FrdRptgRspn.setter
	def FrdRptgRspn(self, value):
		self._FrdRptgRspn = value if type(value) != base_types.auto else self.make_default("FrdRptgRspn")

	@FrdRptgRspn.deleter
	def FrdRptgRspn(self):
		del self._FrdRptgRspn
		self._FrdRptgRspn = None

	@property
	def KeyXchgInitn(self):
		return self._KeyXchgInitn

	@KeyXchgInitn.setter
	def KeyXchgInitn(self, value):
		self._KeyXchgInitn = value if type(value) != base_types.auto else self.make_default("KeyXchgInitn")

	@KeyXchgInitn.deleter
	def KeyXchgInitn(self):
		del self._KeyXchgInitn
		self._KeyXchgInitn = None

	@property
	def KeyXchgRspn(self):
		return self._KeyXchgRspn

	@KeyXchgRspn.setter
	def KeyXchgRspn(self, value):
		self._KeyXchgRspn = value if type(value) != base_types.auto else self.make_default("KeyXchgRspn")

	@KeyXchgRspn.deleter
	def KeyXchgRspn(self):
		del self._KeyXchgRspn
		self._KeyXchgRspn = None

	@property
	def NqryInitn(self):
		return self._NqryInitn

	@NqryInitn.setter
	def NqryInitn(self, value):
		self._NqryInitn = value if type(value) != base_types.auto else self.make_default("NqryInitn")

	@NqryInitn.deleter
	def NqryInitn(self):
		del self._NqryInitn
		self._NqryInitn = None

	@property
	def NqryRspn(self):
		return self._NqryRspn

	@NqryRspn.setter
	def NqryRspn(self, value):
		self._NqryRspn = value if type(value) != base_types.auto else self.make_default("NqryRspn")

	@NqryRspn.deleter
	def NqryRspn(self):
		del self._NqryRspn
		self._NqryRspn = None

	@property
	def NtwkMgmtInitn(self):
		return self._NtwkMgmtInitn

	@NtwkMgmtInitn.setter
	def NtwkMgmtInitn(self, value):
		self._NtwkMgmtInitn = value if type(value) != base_types.auto else self.make_default("NtwkMgmtInitn")

	@NtwkMgmtInitn.deleter
	def NtwkMgmtInitn(self):
		del self._NtwkMgmtInitn
		self._NtwkMgmtInitn = None

	@property
	def NtwkMgmtRspn(self):
		return self._NtwkMgmtRspn

	@NtwkMgmtRspn.setter
	def NtwkMgmtRspn(self, value):
		self._NtwkMgmtRspn = value if type(value) != base_types.auto else self.make_default("NtwkMgmtRspn")

	@NtwkMgmtRspn.deleter
	def NtwkMgmtRspn(self):
		del self._NtwkMgmtRspn
		self._NtwkMgmtRspn = None

	@property
	def RcncltnInitn(self):
		return self._RcncltnInitn

	@RcncltnInitn.setter
	def RcncltnInitn(self, value):
		self._RcncltnInitn = value if type(value) != base_types.auto else self.make_default("RcncltnInitn")

	@RcncltnInitn.deleter
	def RcncltnInitn(self):
		del self._RcncltnInitn
		self._RcncltnInitn = None

	@property
	def RcncltnRspn(self):
		return self._RcncltnRspn

	@RcncltnRspn.setter
	def RcncltnRspn(self, value):
		self._RcncltnRspn = value if type(value) != base_types.auto else self.make_default("RcncltnRspn")

	@RcncltnRspn.deleter
	def RcncltnRspn(self):
		del self._RcncltnRspn
		self._RcncltnRspn = None

	@property
	def RtrvlFlfmtInitn(self):
		return self._RtrvlFlfmtInitn

	@RtrvlFlfmtInitn.setter
	def RtrvlFlfmtInitn(self, value):
		self._RtrvlFlfmtInitn = value if type(value) != base_types.auto else self.make_default("RtrvlFlfmtInitn")

	@RtrvlFlfmtInitn.deleter
	def RtrvlFlfmtInitn(self):
		del self._RtrvlFlfmtInitn
		self._RtrvlFlfmtInitn = None

	@property
	def RtrvlFlfmtRspn(self):
		return self._RtrvlFlfmtRspn

	@RtrvlFlfmtRspn.setter
	def RtrvlFlfmtRspn(self, value):
		self._RtrvlFlfmtRspn = value if type(value) != base_types.auto else self.make_default("RtrvlFlfmtRspn")

	@RtrvlFlfmtRspn.deleter
	def RtrvlFlfmtRspn(self):
		del self._RtrvlFlfmtRspn
		self._RtrvlFlfmtRspn = None

	@property
	def RtrvlInitn(self):
		return self._RtrvlInitn

	@RtrvlInitn.setter
	def RtrvlInitn(self, value):
		self._RtrvlInitn = value if type(value) != base_types.auto else self.make_default("RtrvlInitn")

	@RtrvlInitn.deleter
	def RtrvlInitn(self):
		del self._RtrvlInitn
		self._RtrvlInitn = None

	@property
	def RtrvlRspn(self):
		return self._RtrvlRspn

	@RtrvlRspn.setter
	def RtrvlRspn(self, value):
		self._RtrvlRspn = value if type(value) != base_types.auto else self.make_default("RtrvlRspn")

	@RtrvlRspn.deleter
	def RtrvlRspn(self):
		del self._RtrvlRspn
		self._RtrvlRspn = None

	@property
	def RvslInitn(self):
		return self._RvslInitn

	@RvslInitn.setter
	def RvslInitn(self, value):
		self._RvslInitn = value if type(value) != base_types.auto else self.make_default("RvslInitn")

	@RvslInitn.deleter
	def RvslInitn(self):
		del self._RvslInitn
		self._RvslInitn = None

	@property
	def RvslRspn(self):
		return self._RvslRspn

	@RvslRspn.setter
	def RvslRspn(self, value):
		self._RvslRspn = value if type(value) != base_types.auto else self.make_default("RvslRspn")

	@RvslRspn.deleter
	def RvslRspn(self):
		del self._RvslRspn
		self._RvslRspn = None

	@property
	def SttlmRptgInitn(self):
		return self._SttlmRptgInitn

	@SttlmRptgInitn.setter
	def SttlmRptgInitn(self, value):
		self._SttlmRptgInitn = value if type(value) != base_types.auto else self.make_default("SttlmRptgInitn")

	@SttlmRptgInitn.deleter
	def SttlmRptgInitn(self):
		del self._SttlmRptgInitn
		self._SttlmRptgInitn = None

	@property
	def SttlmRptgRspn(self):
		return self._SttlmRptgRspn

	@SttlmRptgRspn.setter
	def SttlmRptgRspn(self, value):
		self._SttlmRptgRspn = value if type(value) != base_types.auto else self.make_default("SttlmRptgRspn")

	@SttlmRptgRspn.deleter
	def SttlmRptgRspn(self):
		del self._SttlmRptgRspn
		self._SttlmRptgRspn = None

	@property
	def VrfctnInitn(self):
		return self._VrfctnInitn

	@VrfctnInitn.setter
	def VrfctnInitn(self, value):
		self._VrfctnInitn = value if type(value) != base_types.auto else self.make_default("VrfctnInitn")

	@VrfctnInitn.deleter
	def VrfctnInitn(self):
		del self._VrfctnInitn
		self._VrfctnInitn = None

	@property
	def VrfctnRspn(self):
		return self._VrfctnRspn

	@VrfctnRspn.setter
	def VrfctnRspn(self, value):
		self._VrfctnRspn = value if type(value) != base_types.auto else self.make_default("VrfctnRspn")

	@VrfctnRspn.deleter
	def VrfctnRspn(self):
		del self._VrfctnRspn
		self._VrfctnRspn = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='AdddmInitn', type=Max2MBBinary, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='AdddmRspn', type=Max2MBBinary, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Amdmnt', type=Max2MBBinary, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='AuthstnInitn', type=Max2MBBinary, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='AuthstnRspn', type=Max2MBBinary, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='CardMgmtInitn', type=Max2MBBinary, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='CardMgmtRspn', type=Max2MBBinary, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='ChrgBckInitn', type=Max2MBBinary, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='ChrgBckRspn', type=Max2MBBinary, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Err', type=Max2MBBinary, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='FeeColltnInitn', type=Max2MBBinary, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='FeeColltnRspn', type=Max2MBBinary, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='FileActnInitn', type=Max2MBBinary, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='FileActnRspn', type=Max2MBBinary, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='FinInitn', type=Max2MBBinary, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='FinRspn', type=Max2MBBinary, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='FrdDspstnInitn', type=Max2MBBinary, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='FrdDspstnRspn', type=Max2MBBinary, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='FrdRptgInitn', type=Max2MBBinary, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='FrdRptgRspn', type=Max2MBBinary, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='KeyXchgInitn', type=Max2MBBinary, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='KeyXchgRspn', type=Max2MBBinary, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='NqryInitn', type=Max2MBBinary, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='NqryRspn', type=Max2MBBinary, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='NtwkMgmtInitn', type=Max2MBBinary, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='NtwkMgmtRspn', type=Max2MBBinary, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='RcncltnInitn', type=Max2MBBinary, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='RcncltnRspn', type=Max2MBBinary, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='RtrvlFlfmtInitn', type=Max2MBBinary, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='RtrvlFlfmtRspn', type=Max2MBBinary, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='RtrvlInitn', type=Max2MBBinary, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='RtrvlRspn', type=Max2MBBinary, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='RvslInitn', type=Max2MBBinary, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='RvslRspn', type=Max2MBBinary, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='SttlmRptgInitn', type=Max2MBBinary, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='SttlmRptgRspn', type=Max2MBBinary, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='VrfctnInitn', type=Max2MBBinary, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='VrfctnRspn', type=Max2MBBinary, min=0, max=1, mutex_group=1, array=False),
	))